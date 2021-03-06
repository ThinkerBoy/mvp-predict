![Alt text](/mvppredict.png?raw=true "ESPN")

## 2018 - 2019 Predictions

#### These are the weekly predictions for MVP (using last year's successful model):
| `LeBron James` | `Kevin Durant` | `Nikola Jokic` | `Joel Embiid` | `James Harden` |
|:---:|:---:|:---:|:---:|:---:|
| 0.250 | 0.250 | 0.250 | 0.063 | 0.063 |

^ these are updated weekly

#### These predictions were made prior to the start of the season using a _newer approach_ as opposed to last year.

| Player Name        | Rank       | 
|:-------------:|:-------------:| 
| `Giannis Antetokounmpo` | 0.899(1) |
| `LeBron James` | 0.871(2) | 
| `James Harden` | 0.835(3) | 
| `Anthony Davis` | 0.830(4) | 
| `Karl Anthony Towns` | 0.73(5) | 
| `Kawhi Leonard` | 0.55(6) | 
| `Nikola Jokic` | 0.33(7) | 

#### Upon running my new model on last season's (2018) field, these were the results:
| `James Harden` | `Anthony Davis` | `LeBron James` | `Karl Anthony Towns (?)` |
|:---:|:---:|:---:|:---:|
| 1.559(1) | 1.036(2) | 0.799(3) | 0.608(4) |


### Notes

*data/mvpForecast.csv* contains forecasted advanced stats for ESPN's top 20 NBA players of the 2018-2019 season.

*forecast.py* is responsible for generating the aforementioned future stats.

*predict.py* is responsible for ranking the MVP candidates based on the model.

*mvp_statline.py* is an independent script that predicts the per-game and advanced stats of this season's MVP.

#### mvp_statline's predictions for this season's MVP

| `ppg` |  `rpg` |  `apg` | `per` | `vorp` | `+/-` | `ts%` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 28.8 | 7.1 | 7.3 | 29.0 | 8.67 | 10.2 | 0.61 |

## 2017 - 2018 Predictions
Final frontrunner: James Harden

<img src="https://d2cwpp38twqe55.cloudfront.net/req/201810111/images/players/hardeja01.jpg">

| `ppg` | `per` | `vorp` | `+/-` | `ts%` |
|:---:|:---:|:---:|:---:|:---:|
| 30.4 | 29.8 | 8.3 | 10.9 | 0.619 |

### Predictions as of April 12, 2018

| `James Harden` | `LeBron James` | `Anthony Davis` | `Russell Westbrook` |
|:---:|:---:|:---:|:---:|
| 29%(1) | 21%(2) | 14%(3) | 7%(4) |

### In October of 2017, mvp-predict generated this as the projected MVP statline:

| `ppg` | `per` | `vorp` | `+/-` | `ts%` |
|:---:|:---:|:---:|:---:|:---:|
| 27.63 | 29.01 | 8.79 | 10.24 | 0.606 |
