from bankaccount import MinimumBalanceAccount

accountMin = MinimumBalanceAccount(1500, 1000)

result = accountMin.try_withdraw(300)


print(result.message)