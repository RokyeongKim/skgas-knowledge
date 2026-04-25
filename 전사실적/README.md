# SK가스 전사 실적 개요

> 출처: 이사회전략세션 (2026.03.30), 통합S재무회의 (2026.04), SK가스 행복경영캔미팅 (2025.11)

## 사업별 세전이익 추이 (2025~2030)

<div id="chart-annual" style="width:100%;height:420px;margin:16px 0;"></div>

> **데이터 주석**
> GPS (발전) '27~'30 중장기 전망치 미공개 / LNG Biz. '25년은 사업 원년으로 별도 집계 없음
> SK가스 연결 세전이익 '27~'30 미확인 / 사업별 합산 ≠ 연결 전체 (연결조정·미배분 항목 존재)

## '26년 1분기 목표 vs 실적

<div id="chart-q1" style="width:100%;height:320px;margin:16px 0;"></div>

> Trading이 Physical Trading 초과·USD 강세로 목표 대비 +409억
> G&P는 LNG-LPG Optionality 실행(1.5 Cargo)으로 +211억
> Eco Energy는 JKM Unwind 기회 상실·민수 손익 악화로 Δ358억

## 전사 세전이익 요약

| 구분 | '25년 실적 | '26년 목표 | '26년 추정 |
|------|-----------|-----------|-----------|
| **SK가스 연결 세전이익** | **3,142억** | **3,050억** | **4,620억** |
| └ GPS (발전) | 1,304억 | 1,725억 | 1,891억 |
| └ LPG Biz. | 2,132억 | 1,841억 | 미확인 |
| └ LNG Biz. | 미집계 | 143억 | 미확인 |

## 사업별 중기 전망 수치 (억원)

| 사업 | '25실적 | '26목표 | '27전망 | '28전망 | '29전망 | '30전망 |
|------|--------|--------|--------|--------|--------|--------|
| GPS (발전) | 1,304 | 1,725 | 미확인 | 미확인 | 미확인 | 미확인 |
| LPG Biz. | 2,132 | 1,841 | 1,571 | 1,670 | 1,896 | 2,063 |
| LNG Biz. | 미집계 | 143 | 277 | 540 | 859 | 1,075 |

<script>
(function() {
  function initChart(id, option) {
    var dom = document.getElementById(id);
    if (!dom || !window.echarts) {
      setTimeout(function() { initChart(id, option); }, 120);
      return;
    }
    var existing = echarts.getInstanceByDom(dom);
    if (existing) { existing.dispose(); }
    var chart = echarts.init(dom);
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }

  // ── Chart 1: 사업별 세전이익 추이 ──
  initChart('chart-annual', {
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' },
      formatter: function(params) {
        var s = params[0].name + '<br/>';
        params.forEach(function(p) {
          if (p.value !== null && p.value !== undefined) {
            s += p.marker + ' ' + p.seriesName + ': <b>' + p.value.toLocaleString() + '억</b><br/>';
          }
        });
        return s;
      }
    },
    legend: { bottom: 0, type: 'scroll' },
    grid: { left: '3%', right: '4%', bottom: '15%', containLabel: true },
    xAxis: {
      type: 'category',
      data: ["'25실적", "'26목표", "'27전망", "'28전망", "'29전망", "'30전망"]
    },
    yAxis: { type: 'value', name: '억원', nameLocation: 'end',
      axisLabel: { formatter: function(v) { return v.toLocaleString(); } }
    },
    series: [
      {
        name: 'GPS (발전)',
        type: 'bar', stack: 'biz',
        data: [1304, 1725, null, null, null, null],
        itemStyle: { color: '#5470c6' }
      },
      {
        name: 'LPG Biz.',
        type: 'bar', stack: 'biz',
        data: [2132, 1841, 1571, 1670, 1896, 2063],
        itemStyle: { color: '#91cc75' }
      },
      {
        name: 'LNG Biz.',
        type: 'bar', stack: 'biz',
        data: [null, 143, 277, 540, 859, 1075],
        itemStyle: { color: '#fac858' }
      },
      {
        name: 'SK가스 연결 세전이익',
        type: 'line',
        data: [3142, 3050, null, null, null, null],
        lineStyle: { type: 'dashed', width: 2, color: '#ee6666' },
        itemStyle: { color: '#ee6666' },
        symbol: 'circle', symbolSize: 8,
        label: { show: true, position: 'top',
          formatter: function(p) { return p.value ? p.value.toLocaleString() : ''; }
        }
      }
    ]
  });

  // ── Chart 2: '26 1Q 목표 vs 실적 ──
  initChart('chart-q1', {
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' },
      formatter: function(params) {
        var s = params[0].axisValue + '<br/>';
        params.forEach(function(p) {
          s += p.marker + ' ' + p.seriesName + ': <b>' + p.value.toLocaleString() + '억</b><br/>';
        });
        return s;
      }
    },
    legend: { bottom: 0 },
    grid: { left: '3%', right: '10%', bottom: '12%', containLabel: true },
    xAxis: { type: 'value', name: '억원',
      axisLabel: { formatter: function(v) { return v.toLocaleString(); } }
    },
    yAxis: {
      type: 'category',
      data: ['G&P (LNG/LPG Opt.)', 'Trading', 'Eco Energy (LPG)', 'GPS (발전)']
    },
    series: [
      {
        name: '목표',
        type: 'bar',
        data: [61, 525, 508, 542],
        itemStyle: { color: '#ccc' },
        label: { show: true, position: 'right',
          formatter: function(p) { return p.value.toLocaleString() + '억'; }
        }
      },
      {
        name: '실적',
        type: 'bar',
        data: [272, 933, 150, 554],
        itemStyle: {
          color: function(p) {
            var actual = [272, 933, 150, 554];
            var target = [61, 525, 508, 542];
            return actual[p.dataIndex] >= target[p.dataIndex] ? '#5fb552' : '#e05252';
          }
        },
        label: { show: true, position: 'right',
          formatter: function(p) { return p.value.toLocaleString() + '억'; }
        }
      }
    ]
  });
})();
</script>
