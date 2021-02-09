import argparse
from config import api_key, secret_key
from TradingBot import TradingBot
from TriggerBot import TriggerBot

# Positional argument
parser = argparse.ArgumentParser(description="HumpyPump.py is a fast pump bot for buy and sell cryptos")
parser.add_argument('-id',dest="channel_id", type=str , help='ID of discord channel where the buy signal is trigger')
parser.add_argument('-s', dest="separator", type=str, help='Is the trigger signal of buying coin. Example: Buy $SKY in coinbase')
parser.add_argument('-p', dest="profit", type=float, help='Is the multiplicator value of next sell of the cryptos what you buy. Example: if you put 2.00 in this variable and you buy $DOGE at 0.5 $ you sell your $DOGE in 1.00$. A high value incremet the risk of lose your invertion.')

# Optionals argument
parser.add_argument('--fee', dest='fee', help='Is the fee of binance sometimes this changes and you can update', default=0.02)

args = parser.parse_args()
if args.channel_id == None or args.separator == None or args.profit == None:
    parser.print_help()
    exit(1)

trigger_bot = TriggerBot(args.channel_id, args.separator)
trading_bot = TradingBot(api_key=api_key, secret_key=secret_key, profit=args.profit, fee=args.fee)

trigger = True
while trigger:
    messages = trigger_bot.GetMessages()
    for message in messages:
        if trigger_bot.IsValidMessage(message['content']):
            trigger_bot.GetCoinFromMessage(message['content'])
            trigger = False
            break

trading_bot.SetCoin(trigger_bot.coin)
trading_bot.Buy()
trading_bot.Sell()
