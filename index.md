JSON Query Documentation
===================

Querying with JSON Query is super simple

Follow along using the sample JSON here: [http://bit.ly/1OrWKnO ](http://bit.ly/1OrWKnO)

Query any value by key
-----------

**Query**
```
offset 
```
**Results**
```
-8
```

Traverse object trees using the dot operator
-----------

**Query**
```
hourly.icon
```
**Results**
```
rain
```

Query deeper structures
-----------

**Query**
```
hourly.data.ozone
```
**Results**
```
318.97, 318.02
```

Access arrays with indices in square brackets
-----------

**Query**
```
data[1]
```
**Results**
```
{
  "temperature" : 54.65,
  "windSpeed" : 6.87,
  "humidity" : 0.78,
  "windBearing" : 138,
  "cloudCover" : 0.88,
  "time" : 1452628800,
  "dewPoint" : 48.1,
  "summary" : "Mostly Cloudy",
  "icon" : "partly-cloudy-day",
  "precipIntensity" : 0,
  "visibility" : 7.68,
  "ozone" : 318.02,
  "apparentTemperature" : 54.65,
  "pressure" : 1022.38,
  "precipProbability" : 0
}
```

Mix and match arrays with dot operators
-----------

**Query**
```
hourly.data[1].ozone
```
**Results**
```
318.02
```

Parent elements are not always required
-----------

**Query**
```
data[1].ozone
```
**Results**
```
318.02
```