from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests, urllib3
import requests
import nopecha
import time
import json
import random
import string
ADMIN_USER_ID = 5244246071
TOKEN: Final = '6352978480:AAH8SlUG_PRCaqrCJHv2px-ROwmYZ8qNftU'
def bypass(email,passs,token):
    data = {
    "email": email,
    "password": passs,
    "tos_accepted": True,
    "recaptcha": token
  }
    response1 = requests.post("https://proxy.webshare.io/api/v2/register/", json=data)
    response_json = response1.json()
    tokenacc = response_json.get("token")
    url = "https://proxy.webshare.io/api/v2/proxy/config/"
    headers = {
    "Authorization": f"Token {tokenacc}"
}
    response = requests.get(url, headers=headers)
    data = response.json()
    username = data.get("username")
    password = data.get("password")
    send=f"p.webshare.io:80:{username}-rotate:{password}"
    return send
async def gen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_USER_ID:await update.message.reply_text("You are not authenticated to use the bot ❌")
    else:
        await update.message.reply_text("Solving Captcha...")
    rdne = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
    email = f"memcho{rdne}@gmail.com"
    rdnp = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=5))
    passs = f"mcxdwsps{rdnp}"
    timer = round(random.uniform(0.00, 10.50), 2)
    try:
        nopecha.api_key = 'sub_1P96QLCRwBwvt6ptrXmnmbN2'
        token = nopecha.Token.solve(
            type='recaptcha2',
            sitekey='6LeHZ6UUAAAAAKat_YS--O2tj_by3gv3r_l03j9d',
            url='https://proxy2.webshare.io/register?'
)
        await update.message.reply_text(f"Done solve!!")
        pxy=bypass(email,passs,token)
        await update.message.reply_text(f'''
→ WebShare Proxy
→ Limit: 1/1
                                        
• Proxy: {pxy}
• Email: {email}
• Password: {passs}
• Status: Live ✅  

→ Time: {timer} seconds
→ Checked By: {user_id} [Owner]                                   
''')
    except:
        await update.message.reply_text(f"Error solve Captcha. ❌")
        return
async def startcm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    await update.message.reply_text(f'''
Hi {user_id}
━━━━━━━━━━━━━━
<code> To start generate webshare.io account. </code>
Type /ws ✅
━━━━━━━━━━━━━━
Bot by MemChoXD''')
if __name__=='__main__':
    print('Wibu is on top 10%....')
    app=Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', startcm))
    app.add_handler(CommandHandler('ws', gen))
    print('.....100%')
    app.run_polling(poll_interval=3)
