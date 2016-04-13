## Rainfall: Map, Filter, Reduce
h/t [@selassid](https://github.com/selassid/codeguild/blob/master/practice-rain.md)

This exercise introduces the concepts of map, filter and reduce in js using rainfall [data](http://or.water.usgs.gov/non-usgs/bes/) provided by the city of Portland.
___

The rainfall data is stored in `mt_tabor.rain.js` as the `rainfall` variable. `rainfall` contains an array of objects that specify date and hourly rainfall data in 0.1 inch increments as such:
```js
  var rainfall = [
    ...
    {
      date: '01-APR-2016' // %d-%b-%Y,
      hourly: [0, 5, ... 0 ]
    }
    ...
  ]
```

### Steps
In `analyze.js` complete the following using map, filter and reduce:
* compute and console.log daily totals of rainfall
* compute and console.log cumulative rainfall in 2016 so far
* challenge: compute and console.log cumulative rainfall for each year
* compute and console.log total rainfall in Nov of 1998 and 2008
* challenge: compute and console.log average rainfall for each month, i.e. average Jan, .. Dec from each year with complete data
* challenge: compute and console.log the month with the most rainfall

### Advanced
Render svg bar charts to visualize rainfall by month and by year.
