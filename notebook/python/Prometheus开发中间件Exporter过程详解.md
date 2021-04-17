Prometheus 为开发这提供了客户端工具，用于为自己的中间件开发Exporter，对接Prometheus 。

目前支持的客户端

  * [ Go ](https://links.jianshu.com/go?to=http%3A%2F%2Fgodoc.org%2Fgithub.com%2Fprometheus%2Fclient_golang%2Fprometheus%23Counter)
  * [ Java ](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fprometheus%2Fclient_java%2Fblob%2Fmaster%2Fsimpleclient%2Fsrc%2Fmain%2Fjava%2Fio%2Fprometheus%2Fclient%2FCounter.java)
  * [ Python ](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fprometheus%2Fclient_python%23counter)
  * [ Ruby ](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fprometheus%2Fclient_ruby%23counter)

以go为例开发自己的Exporter

依赖包的引入

工程结构

> [root@node1 data]# tree exporter/  
>  exporter/  
>  ├── collector  
>  │ └── node.go  
>  ├── go.mod  
>  └── main.go

引入依赖包

```python

    require (
      github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
      github.com/modern-go/reflect2 v1.0.1 // indirect
      github.com/prometheus/client_golang v1.1.0
        //借助gopsutil 采集主机指标
      github.com/shirou/gopsutil v0.0.0-20190731134726-d80c43f9c984
    )
```

main.go

```python

    package main
    
    import (
      "cloud.io/exporter/collector"
      "fmt"
      "github.com/prometheus/client_golang/prometheus"
      "github.com/prometheus/client_golang/prometheus/promhttp"
      "net/http"
    )
    
    func init() {
       //注册自身采集器
      prometheus.MustRegister(collector.NewNodeCollector())
    }
    func main() {
      http.Handle("/metrics", promhttp.Handler())
      if err := http.ListenAndServe(":8080", nil); err != nil {
        fmt.Printf("Error occur when start server %v", err)
      }
    }
```

为了能看清结果我将默认采集器注释,位置registry.go

```python

    func init() {
      //MustRegister(NewProcessCollector(ProcessCollectorOpts{}))
      //MustRegister(NewGoCollector())
    }
```

/collector/node.go

代码中涵盖了Counter、Gauge、Histogram、Summary四种情况，一起混合使用的情况，具体的说明见一下代码中。

```python

    package collector
    
    import (
      "github.com/prometheus/client_golang/prometheus"
      "github.com/shirou/gopsutil/host"
      "github.com/shirou/gopsutil/mem"
      "runtime"
      "sync"
    )
    
    var reqCount int32
    var hostname string
    type NodeCollector struct {
      requestDesc  *prometheus.Desc  //Counter
      nodeMetrics   nodeStatsMetrics //混合方式 
      goroutinesDesc *prometheus.Desc  //Gauge
      threadsDesc  *prometheus.Desc //Gauge
      summaryDesc  *prometheus.Desc //summary
      histogramDesc *prometheus.Desc  //histogram
      mutex     sync.Mutex
    }
    //混合方式数据结构
    type nodeStatsMetrics []struct {
      desc  *prometheus.Desc
      eval  func(*mem.VirtualMemoryStat) float64
      valType prometheus.ValueType
    }
    
    //初始化采集器
    func NewNodeCollector() prometheus.Collector {
      host,_:= host.Info()
      hostname = host.Hostname
      return &NodeCollector{
        requestDesc: prometheus.NewDesc(
          "total_request_count",
          "请求数",
          []string{"DYNAMIC_HOST_NAME"}, //动态标签名称
          prometheus.Labels{"STATIC_LABEL1":"静态值可以放在这里","HOST_NAME":hostname}),
        nodeMetrics: nodeStatsMetrics{
          {
            desc: prometheus.NewDesc(
              "total_mem",
              "内存总量",
              nil, nil),
            valType: prometheus.GaugeValue,
            eval: func(ms *mem.VirtualMemoryStat) float64 { return float64(ms.Total) / 1e9 },
          },
          {
            desc: prometheus.NewDesc(
              "free_mem",
              "内存空闲",
              nil, nil),
            valType: prometheus.GaugeValue,
            eval: func(ms *mem.VirtualMemoryStat) float64 { return float64(ms.Free) / 1e9 },
          },
    
        },
        goroutinesDesc:prometheus.NewDesc(
          "goroutines_num",
          "协程数.",
          nil, nil),
        threadsDesc: prometheus.NewDesc(
          "threads_num",
          "线程数",
          nil, nil),
        summaryDesc: prometheus.NewDesc(
          "summary_http_request_duration_seconds",
          "summary类型",
          []string{"code", "method"},
          prometheus.Labels{"owner": "example"},
        ),
        histogramDesc: prometheus.NewDesc(
          "histogram_http_request_duration_seconds",
          "histogram类型",
          []string{"code", "method"},
          prometheus.Labels{"owner": "example"},
        ),
      }
    }
    
    // Describe returns all descriptions of the collector.
    //实现采集器Describe接口
    func (n *NodeCollector) Describe(ch chan<- *prometheus.Desc) {
      ch <- n.requestDesc
      for _, metric := range n.nodeMetrics {
        ch <- metric.desc
      }
      ch <- n.goroutinesDesc
      ch <- n.threadsDesc
      ch <- n.summaryDesc
      ch <- n.histogramDesc
    }
    // Collect returns the current state of all metrics of the collector.
    //实现采集器Collect接口,真正采集动作
    func (n *NodeCollector) Collect(ch chan<- prometheus.Metric) {
      n.mutex.Lock()
      ch <- prometheus.MustNewConstMetric(n.requestDesc,prometheus.CounterValue,0,hostname)
      vm, _ := mem.VirtualMemory()
      for _, metric := range n.nodeMetrics {
        ch <- prometheus.MustNewConstMetric(metric.desc, metric.valType, metric.eval(vm))
      }
    
      ch <- prometheus.MustNewConstMetric(n.goroutinesDesc, prometheus.GaugeValue, float64(runtime.NumGoroutine()))
    
      num, _ := runtime.ThreadCreateProfile(nil)
      ch <- prometheus.MustNewConstMetric(n.threadsDesc, prometheus.GaugeValue, float64(num))
    
      //模拟数据
      ch <- prometheus.MustNewConstSummary(
        n.summaryDesc,
        4711, 403.34,
        map[float64]float64{0.5: 42.3, 0.9: 323.3},
        "200", "get",
      )
    
      //模拟数据
      ch <- prometheus.MustNewConstHistogram(
          n.histogramDesc,
          4711, 403.34,
          map[float64]uint64{25: 121, 50: 2403, 100: 3221, 200: 4233},
          "200", "get",
        )
      n.mutex.Unlock()
    }
```

执行的结果 [ http://127.0.0.1:8080/metrics
](https://links.jianshu.com/go?to=http%3A%2F%2F127.0.0.1%3A8080%2Fmetrics)

![](https://img.jbzj.com/file_images/article/202011/2020113091638031.png?2020103091649)

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

