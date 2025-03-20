# emoji = {
#     "sad": ":(",
#     "happy": ":)",
#     "ok": "-_-"
# }
#
# user_input = input("How are you today?").lower()
#
# if "sad" in user_input:
#     print(user_input.replace("sad",emoji.get("sad")))
# elif "happy" in user_input:
#     print(user_input.replace("happy",emoji.get("happy")))
# elif "ok" in user_input:
#     print(user_input.replace("ok",emoji.get("ok")))
# else:
#     print("Don't you have emotions?")
#

emoji = {
    "sad": ":(",
    "happy": ":)",
    "ok": "-_-"
}

user_input = input("How are you today?").lower()

words = (user_input.split())

op = ""
for word in words:
    op += emoji.get(word, word) + " "
print(op)

