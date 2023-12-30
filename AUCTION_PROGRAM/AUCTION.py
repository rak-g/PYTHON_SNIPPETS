import LOGO

print(LOGO.logo)

bids = {}
bidding_finished = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = input("What is your bid?: $ ")
    bids[name] = price
    should_continue = input("Are there any other bidders?Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        continue
    else:
        print("Please enter valid option")
