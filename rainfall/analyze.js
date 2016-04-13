console.log(rainfall)

var dailyTotals =
  rainfall
    .map(function (day) {
      return day.hourly.reduce(function (a, b) {
        return a + b;
      })
    })

console.log(dailyTotals)
