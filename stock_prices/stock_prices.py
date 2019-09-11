#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_arr = []
  for i in range(len(prices)):
    for j in range(0, len(prices) - 1):
      if i > j:
        max_arr.append(prices[i]-prices[j])

  max_profit = max(max_arr)
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))