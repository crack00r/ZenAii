#!/bin/bash
# Will only install apt packages on first run 
if [ ! -f .GUI_INSTALLED ]; then
    sudo apt install -y dialog jq curl
   touch .GUI_INSTALLED
fi
sudo rm -rf pairs.txt
sudo rm -rf bitpairs.txt
sudo rm -rf gdpairs.txt
sudo rm -rf krpairs.txt
sudo rm -rf commands.sh

intro="Welcome to the Zenbot GUI. Please read the next page carefully as it will list the strategies and any commands needed. Hit the right button to select OK. UP and DOWN to scroll."
strategies=$(\
  whiptail --title "Zenbot GUI" \
          --scrolltext \
         --msgbox "$intro" 20 40 \
  3>&1 1>&2 2>&3 3>&- \
)

cmd=(dialog --separate-output --checklist "Trade or run Simulation or run Backfill?" 22 76 16)
options=(
        trade trade off
		backfill backfill off
		sim sim off
		)
choices=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)
for choice in $choices
do
    case $choice in
        trade)
            com=trade
            ;;
		backfill)
            com=backfill
            ;;
		sim)
            com=sim
            ;;
    esac
done



value1="$(./zenbot.sh list-strategies)"
strategies=$(\
  whiptail --title "Strategy Info" \
          --scrolltext \
         --msgbox "$value1" 50	100 \
  3>&1 1>&2 2>&3 3>&- \
)

cmd=(dialog --separate-output --checklist "Select Strategy or none for backfill:" 22 76 16)
options=(
        macd macd off
        Stochastic Stochastic off
        rsi rsi off
        sar sar off
        speed speed off
        rsi_macd rsi_macd off
        trend_ema trend_ema off
        macd macd off)
choices=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)
for choice in $choices
do
    case $choice in
        Stochastic)
            strat=--strategy=Stochastic
            ;;
        macd)
            strat=--strategy=macd
            ;;
        rsi)
            strat=--strategy=rsi
            ;;
        sar)
            strat=--strategy=sar
            ;;
        speed)
            strat=--strategy=speed
            ;;
        rsi_macd)
            strat=--strategy=rsi_macd
            ;;
        trend_ema)
            strat=--strategy=trend_ema
            ;;
        macd)
            strat=--strategy=macd
            ;;
    esac
done



cmd=(dialog --separate-output --checklist "Select period or none for backfill:" 22 76 16)
options=(
        1m 1m off
		2m 2m off
		3m 3m off
		4m 4m off
		5m 5m off
		6m 6m off
		7m 7m off
		8m 8m off
		9m 9m off
		10m 10m off
		15m 15m off
		20m 20m off
		25m 25m off
		30m 30m off
		35m 35m off
		40m 40m off
		45m 45m off
		50m 50m off
		55m 55m off
		60m 60m off
		65m 65m off
		70m 70m off
		75m 75m off
		80m 80m off
		85m 85m off
		90m 90m off
		95m 95m off
		100m 100m off
		105m 105m off
		110m 110m off
		115m 115m off
		120m 120m off)
choices=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)
for choice in $choices
do
    case $choice in
        *)
            per=--period=$choice
            ;;
    esac
done

extra=$(\
  dialog --title "Input other -- commands for your strategy here" \
         --inputbox "Enter the -- command:" 8 40 \
  3>&1 1>&2 2>&3 3>&- \
)

cmd=(dialog --separate-output --checklist "Select Coins to Trade:" 22 76 16)
set -e
i=0
master="$(curl -k 'https://poloniex.com/public?command=returnTicker&period=60' | jq '. | keys | .' | sed 's/\"//g' | sed 's/\,//g' | sed 's/\]//g' | sed 's/\[//g')"
for KEY in $master
        do 
        i=$((i+1))
        echo Poloniex."$KEY" Poloniex."$KEY" off
        done > pairs.txt
bitfinex="$(curl -k 'https://api.bitfinex.com/v1/symbols' | jq '. | . | .' | sed 's/\"//g' | sed 's/\,//g' | sed 's/\]//g' | sed 's/\[//g')"
for KEY in $bitfinex
        do
        i=$((i+1))
        echo Bitfinex."$KEY" Bitfinex."$KEY" off
        done > bitpairs.txt
gdax="$(curl -k 'https://api.gdax.com/products' | jq '.[] .id' | sed 's/\"//g' | sed 's/\,//g' | sed 's/\]//g' | sed 's/\[//g')"
for KEY in $gdax
        do
        i=$((i+1))
        echo Gdax."$KEY" Gdax."$KEY" off
        done > gdpairs.txt
gdax="$(curl -k 'https://api.kraken.com/0/public/AssetPairs' | jq '.result | keys | .' | sed 's/\"//g' | sed 's/\,//g' | sed 's/\]//g' | sed 's/\[//g' | sed 's/\.d//g')"
for KEY in $gdax
        do
        i=$((i+1))
        echo Kraken."$KEY" Kraken."$KEY" off
        done > krpairs.txt
value=$(<pairs.txt)
bit=$(<bitpairs.txt)
gd=$(<gdpairs.txt)
kr=$(<krpairs.txt)
options=(
	$value
	$bit
	$gd
	$kr)
choices=$("${cmd[@]}" "${options[@]}" 2>&1 >/dev/tty)
clear
for choice in $choices
do
    case $choice in
	*)
            echo PreLoading Coin Please Wait 61s for proxy catchup
            sleep 61
            if [[ $choice == *"Poloniex.BTC"* ]]; then
              choice="$(echo "$choice" | sed 's/BTC_//')"
              BTC=-BTC
              choice=$choice$BTC
              echo $choice
            fi
            if [[ $choice == *"Bitfinex."* ]]; then
              echo $choice
            fi
            if [[ $choice == *"Gdax."* ]]; then
              echo $choice
            fi
            if [[ $choice == *"Kraken."* ]]; then
              echo $choice
            fi
            ./zenbot.sh $com $per $strat $extra $choice &
            ;;
    esac
done
echo DONE will implement screen later

