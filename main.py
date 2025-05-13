from pyrogram import Client, types, enums, filters, compose
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.handlers import MessageHandler
from pyrogram.types.input_media import *
import traceback
import threading
import jdatetime
import datetime
import schedule
import psutil
import random
import string
import json
import time
import sys
import os


start_fmt = "%Y/%m/%d - %H:%M:%S"
history_fmt = "%d_%m_%Y"
jhistory_fmt = "%Y_%m_%d"
fmt = "%H:%M:%S"
IKB = InlineKeyboardButton
IKM = InlineKeyboardMarkup
IMD = InputMediaDocument
IMP = InputMediaPhoto
IMV = InputMediaVideo
IMAN = InputMediaAnimation
IMAU = InputMediaAudio
URL = enums.MessageEntityType.URL
CHANNEL = enums.ChatType.CHANNEL
GROUP = enums.ChatType.GROUP
SUPERGROUP = enums.ChatType.SUPERGROUP
PRIVATE = enums.ChatType.PRIVATE
event = threading.Event()
Tbots_dir = "TabchiBots"


if not os.path.isdir(Tbots_dir):
    os.makedirs(Tbots_dir, exist_ok=True)
    print(f"Created Dir: {Tbots_dir}")


def get_bot_info(tbot_id):
    filename = "TBOT-{}.json".format(tbot_id)
    filename = os.path.join(Tbots_dir, filename)
    with open(filename, encoding="UTF-8") as gtinfo:
        bot_info = json.load(gtinfo)
    return bot_info


def get_tclient(bot_id):
    bot_id = str(bot_id)
    return BOTS[bot_id]


def save_bot_info(tbot_json):
    bot_id = tbot_json["id"]
    if "client" in tbot_json:
        tbot_json.pop("client")
    try:
        filename = "TBOT-{}.json".format(bot_id)
        filename = os.path.join(Tbots_dir, filename)
        with open(filename, "w", encoding="UTF-8") as stinfo:
            json.dump(tbot_json, stinfo, indent=2, ensure_ascii=False)
        print("Saved {} data".format(bot_id))
    except:
        print("Failed to save {} data".format(bot_id))


def get_tbot_files():
    tbot_ids = [x[5:-5] for x in os.listdir(Tbots_dir) if x.startswith("TBOT-") and x.endswith(".json")]
    return tbot_ids


def load_tabchis():
    tbot_ids = get_tbot_files()
    print(f"tbot_ids: {tbot_ids}")
    faied_bots = []
    f = 1
    installed_bots = []
    i = 1
    if len(tbot_ids) != 0:
        for tbot_id in tbot_ids:
            print(f"tbid: {tbot_id}")
            bot_info = get_bot_info(tbot_id)
            tta = "{}. {} | {}".format(i, bot_info["mention"], bot_info["id"])
            name = bot_info["name"]
            bot_id = bot_info["id"]
            session_string = bot_info["session_string"]
            try:
                if os.path.isfile(f"{name}.session"):
                    tmp_client = Client(name=name, proxy=proxy)
                    print("bot {} loaded normally".format(bot_id))
                else:
                    tmp_client = Client(name=name, session_string=session_string, proxy=proxy)
                    tmp_client.start()
                    tmp_client.stop()
                    print("bot {} loaded with session_string".format(bot_id))
                BOTS[str(bot_id)] = tmp_client
                if not bot_info["installed"]:
                    bot_info["installed"] = True
                    installed_bots.append(tta)
                    i += 1
                    save_bot_info(bot_info)
            except:
                f += 1
                tta = "{}. {} | {}".format(f, bot_info["mention"], bot_info["id"])
                faied_bots.append(tta)
    text = ""
    if len(faied_bots) != 0 or len(installed_bots) != 0:
        bot.start()
        fta = "\n".join(faied_bots)
        ita = "\n".join(installed_bots)
        if len(installed_bots) != 0:
            text += "تبچی (های) زیر با موفقیت نصب شدند:\n{}".format(ita)
        if len(faied_bots) != 0:
            text += "خطایی در لود شدن تبچی های زیر رخ داد:\n{}".format(fta) + "\nپیشنهاد میشود تبچی این تبچی (ها) را از پنل مدیریت حذف و مجدد نصب کنید."
        # text = "خطایی در لود شدن تبچی های زیر رخ داد.\n\n{}".format(tta)
        bot.send_message(chat_id=Admin, text=text)
        bot.stop()


def nowtime():
    # Tehran_TZ
    Time = datetime.datetime.now()
    return Time


def jnowtime():
    # Tehran_TZ
    Time = jdatetime.datetime.now()
    return Time




ManiJ = DEVELOPER = 5635247680
print(f"Developed tavasote Mani_AZ09. telegram: https://t.me/Mani_Je & {ManiJ}")
proxy = None
Admin = 5635247680
api_id: int = 24226163
api_hash: str = "56b2740d5ebf32cbee22c8df22e5e2d0"
bot_token: str = "7034994099:AAGMDQmkf_K_pR_DwPDOTTb5pJ1UkFxCA3c"
bot = Client(name="TabChi3", api_hash=api_hash, api_id=api_id, proxy=proxy, bot_token=bot_token)
main_command = "manage"
bot.start()
start_time = jnowtime()
bot.send_message(chat_id=Admin, text="\n".join(["ربات اصلی استارت شد.", str(start_time.strftime(start_fmt)), "مدیریت بات ها:", f"/{main_command}", "مصرف منابع:", "/resources"]))
mainbot_info: types.User = bot.get_me()
bot.stop()
BOTS = {}
tmp_bots = []
load_tabchis()
M = types.Message


CHAT_FILE = "CHAT.json"
with open(CHAT_FILE) as cfr:
    chats_to_join: list = json.load(cfr)
TABLIGHAT_FILE = "TABLIGHAT.json"
with open(TABLIGHAT_FILE) as gfr:
    gps_to_join: list = json.load(gfr)
ALLCHATSTOJOIN = chats_to_join + gps_to_join
Timing_file = "Timing.txt"
if not os.path.isfile(Timing_file):
    with open(Timing_file, "w") as tw_:
        tw_.write("0")


def slice_into_pairs(input_list, n=2):
    return [input_list[i:i+n] for i in range(0, len(input_list), n)]


def btt(tof: bool, true="روشن🌞", false="خاموش🌚"):
    if tof:
        return true
    else:
        return false


def inverseb(tof: bool):
    if tof:
        return False
    else:
        return True


def REWPN(input_string):
    input_string = str(input_string)
    # replace_english_with_persian_numbers
    english_to_persian = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹'
    }
    output_string = ''.join(english_to_persian.get(char, char) for char in input_string)

    return output_string


def get_file_info(message: M):
    file_info = False
    m = message
    if m.document:
        file_info = m.document
    if m.video_note:
        file_info = m.video_note
    if m.video:
        file_info = m.video
    if m.photo:
        file_info = m.photo
    if m.animation:
        file_info = m.animation
    if m.sticker:
        file_info = m.sticker
    if m.voice:
        file_info = m.voice
    if m.audio:
        file_info = m.audio
    if m.text:
        file_info = m.text
    return file_info


def isadmin(user_id):
    user_id = int(user_id)
    if user_id == Admin:
        """ادمین درجه یک / ادمین اصلی بات"""
        return 1
    else:
        """نا ادمین / کاربر معمولی"""
        return 0


def istadmin(user_id, tbot_id=None):
    user_id = int(user_id)
    if user_id == Admin:
        """ادمین درجه یک / ادمین اصلی بات"""
        return 1

    if not tbot_id:
        return 0
    bot_info = get_bot_info(tbot_id=tbot_id)
    admins = bot_info["admins"]
    if user_id in admins:
        """ادمین درجه دو / ادمین های تعریف شده توسط ادمین درجه یک"""
        return 2
    else:
        """نا ادمین / کاربر معمولی"""
        return 0


def mention_maker(name, user_id):
    """[name]((tg://user?id=id)"""
    return f"[{name}](tg://user?id={user_id})"


def date_from_timestamp(timestamp, date_format=None):
    ttr = jdatetime.datetime.utcfromtimestamp(timestamp=timestamp)
    if date_format:
        ttr = ttr.strftime(date_format)
    return ttr


def convert_bytes_to_human_readable_size(bytes_input, lang="en"):
    if bytes_input < 0:
        return "Input should be a non-negative number of bytes."

    if lang == "en":
        size_units = ['B', 'KB', 'MB', 'GB']
    if lang == "fa":
        size_units = ['بایت', 'کیلوبایت', 'مگ', 'گیگ']

    threshold = 1024

    size = bytes_input
    unit_index = 0
    while size >= threshold and unit_index < len(size_units) - 1:
        size /= threshold
        unit_index += 1

    result = "{:.1f} {}".format(size, size_units[unit_index])
    return result


cbthrs = convert_bytes_to_human_readable_size


start_text = "\n".join(["به ربات مدیر تبچی خوش آمدید، لطفا از لیست زیر دستور مورد نظر خود رو انتخاب کنید.",
                          "مدیریت تبچی ها:",
                          f"/{main_command}",
                          "مصرف ریسورس های هاست/سرور:",
                          "/resources",
                        ])


def bots_info_list(user_id):
    tbot_ids = get_tbot_files()
    buttons = []
    if len(tbot_ids) != 0:
        text = "💡اطلاعات تبچی(ها)\n"
        for tid in tbot_ids:
            bot_info = get_bot_info(tid)
            if not istadmin(user_id=user_id, tbot_id=tid):
                continue
            name = bot_info["name"]
            bot_id = bot_info["id"]
            username = bot_info["username"]
            tclient = get_tclient(bot_id=bot_id)
            try:
                tclient.start()
            except:
                pass
            bta = [IKB(text="{} | {}".format(username, tid), callback_data=f"tabchi_panel_{tid}")]
            buttons.append(bta)
    else:
        text = "در حال حاضر تبچی ای ثبت نشده"

    buttons.append([IKB(text="افزودن", callback_data="add_tabchi")])
    reply_markup = IKM(buttons)
    return text, reply_markup


def get_string_urls(message: M):
    urls = []
    strng = None
    entities = None
    if message.text:
        strng = message.text
        entities = message.entities
    if message.caption:
        strng = message.caption
        entities = message.caption_entities
    if entities:
        for entity in entities:
            print(entity)
            if entity.type == URL:
                es, el = entity.offset, entity.length
                url = strng[es: es+el]
                urls.append(url)

    return urls


def join_chats(client: Client, urls, time_to_wait=360):
    urls = list(set(urls))
    for url in urls:
        try:
            result: types.Chat = client.join_chat(url)
            if result.type not in [GROUP, SUPERGROUP]:
                result.leave()
                continue
            bot_info = get_bot_info(tbot_id=client.me.id)
            bot_info["gps"].append(result.id)
            save_bot_info(bot_info)
            client.send_message(chat_id="me", text=f"#Joined {url}")
            event.wait(time_to_wait)
        except:
            client.send_message(chat_id="me", text=f"#FailedToJoin {url}")


def tabchi_send_post(client: Client, from_chat_id, msg_id, target_chat_id, quote):
    msg: M = client.get_messages(chat_id=from_chat_id, message_ids=msg_id)
    if msg.media_group_id:
        captions, captions_entities = [], []
        msgs = client.get_media_group(chat_id=from_chat_id, message_id=msg_id)
        gp_msg_ids = []
        for msg in msgs:
            captions.append(msg.caption)
            captions_entities.append(msg.caption_entities)
            gp_msg_ids.append(msg.id)
        if quote:
            client.forward_messages(chat_id=target_chat_id, from_chat_id=from_chat_id, message_ids=gp_msg_ids)
        else:
            client.copy_media_group(chat_id=target_chat_id, from_chat_id=from_chat_id, message_id=msg_id, captions=captions)
    else:
        if msg.media:
            caption = msg.caption
            caption_entities = msg.caption_entities
            if quote:
                client.forward_messages(chat_id=target_chat_id, from_chat_id=from_chat_id, message_ids=msg_id)
            else:
                msg.copy(chat_id=target_chat_id, caption=caption, caption_entities=caption_entities)
        else:
            if quote:
                client.forward_messages(chat_id=target_chat_id, from_chat_id=from_chat_id, message_ids=msg_id)
            else:
                client.send_message(chat_id=target_chat_id, text=msg.text, entities=msg.entities)



@bot.on_message(group=2)
def main_bot_handler2(client: Client, update: M):
    user = update.from_user
    strid = str(user.id)

    if update.text:
        chiz_ersali = update.text
    else:
        chiz_ersali = get_file_info(update).file_id

    if new_auto_message.get(strid, None):
        if update.text:
            tedad = update.text
            if tedad == "-1":
                new_auto_message.pop(strid)
                update.reply_text(text="عملیات لغو شد.")
                return
            if tedad.isdigit():
                tedad = int(tedad)
                if 0 <= tedad <= 100:
                    tbot_id, msg = new_auto_message[strid].values()
                    bot_info = get_bot_info(tbot_id)
                    bot_info["auto_message"] = tedad
                    save_bot_info(tbot_json=bot_info)
                    update.reply_text(text="شدت ارسال پیام تبچی آپدیت شد.\nشدت فعلی: {}/100".format(tedad))
                    text, reply_markup = tabchi_info(tbot_id)
                    msg.edit_text(text=text, reply_markup=reply_markup)
                    new_auto_message.pop(strid)
                else:
                    update.reply_text(text="لطفا فقط یک عدد بین 0 تا 100 ارسال کنید، برای لغو عملیات عدد -1 را ارسال کنید.")
        else:
            update.reply_text(text="لطفا فقط یک عدد بین 0 تا 100 ارسال کنید، برای لغو عملیات عدد -1 را ارسال کنید.")

    if new_auto_reaction.get(strid, None):
        if update.text:
            tedad = update.text
            if tedad == "-1":
                new_auto_reaction.pop(strid)
                update.reply_text(text="عملیات لغو شد.")
                return
            if tedad.isdigit():
                tedad = int(tedad)
                if 0 <= tedad <= 100:
                    tbot_id, msg = new_auto_reaction[strid].values()
                    bot_info = get_bot_info(tbot_id)
                    bot_info["auto_reaction"] = tedad
                    save_bot_info(tbot_json=bot_info)
                    update.reply_text(text="شدت ارسال پیام تبچی آپدیت شد.\nشدت فعلی: {}/100".format(tedad))
                    text, reply_markup = tabchi_info(tbot_id)
                    msg.edit_text(text=text, reply_markup=reply_markup)
                    new_auto_reaction.pop(strid)
                else:
                    update.reply_text(text="لطفا فقط یک عدد بین 0 تا 100 ارسال کنید، برای لغو عملیات عدد -1 را ارسال کنید.")
        else:
            update.reply_text(text="لطفا فقط یک عدد بین 0 تا 100 ارسال کنید، برای لغو عملیات عدد -1 را ارسال کنید.")

    if new_leave.get(strid, None):
        if update.text:
            tedad = update.text
            tbot_id, chat_type = new_leave[strid].values()
            if tedad.isdigit():
                tedad = int(tedad)
                if tedad == 0:
                    new_leave.pop(strid)
                    update.reply_text(text="عملیات لغو شد.")
                    return
                bot_info = get_bot_info(tbot_id)
                chats: list = bot_info[chat_type]
                lenchat = len(chats)
                tbot = get_tclient(bot_id=tbot_id)
                if tedad > lenchat:
                    update.reply_text(text="عدد {} از تعداد چت ها بیشتر است! حداکثر عدد ورودی باید {} باشد.".format(tedad, lenchat))
                    return
                text = ["تبچی با موفقیت از چت های زیر خارج شد و آیدی چت ها از دیتابیس حذف شد."]
                for i in range(tedad):
                    chat_id = chats[i]
                    try:
                        tbot.leave_chat(chat_id=chat_id)
                    except:
                        pass
                    tta = f"{i + 1}. `{chat_id}`"
                    text.append(tta)
                    chats.pop(i)
                text = "\n".join(text)
                bot_info[chat_type] = chats
                save_bot_info(tbot_json=bot_info)
                update.reply_text(text=text)
                new_leave.pop(strid)
            else:
                update.reply_text(text="لطفا فقط عدد ارسال کنید، برای لغو عملیات عدد 0 را ارسال کنید.")
        else:
            update.reply_text(text="لطفا فقط عدد ارسال کنید، برای لغو عملیات عدد 0 را ارسال کنید.")

    if new_gp.get(strid, None):
        if update.text:
            chat_url = update.text
            if chat_url == "-1":
                new_gp.pop(strid)
                update.reply_text(text="عملیات لغو شد.")
                return
            tbot_id, msg = new_gp[strid].values()
            tbot: Client = get_tclient(bot_id=tbot_id)
            try:
                try:
                    tbot.start()
                except:
                    pass
                joined_chat: types.Chat = tbot.join_chat(chat_url)
                update.reply_text(text="تبچی با موفقیت عضو چت {} شد.".format(joined_chat.title))
                new_gp.pop(strid)
            except Exception as E:
                ttt = ["عضو شدن به چت مورد نظر با لینک/آیدی {} با خطای زیر مواجه شد.".format(chat_url),
                       f"\n`{E}`\n",
                       "برای لغو عملیات عدد -1 را ارسال کنید."]
                update.reply_text(text="\n".join(ttt))
                pass
        else:
            update.reply_text(text="لطفا لینک/آیدی گروه مورد نظر را به صورت متنی بفرستید\nبرای لغو عملیات عدد -1 را ارسال کنید.")

    if new_psettins.get(strid, None):
        if update.text:
            mins = update.text
            tabchi_id, msg = new_psettins[strid].values()
            if mins == "-1":
                new_psettins.pop(strid)
                update.reply_text(text="عملیات لغو شد.")
            else:
                if mins.isdigit():
                    bot_info = get_bot_info(tabchi_id)
                    mins = int(mins)
                    amins = bot_info["posts_settings"]["duration"]
                    text = ""
                    if mins == amins:
                        text += "این که همونه ولی درک میکنم کار از محکم کاری عیب نمیکنه\n"
                    bot_info["posts_settings"]["duration"] = mins
                    save_bot_info(bot_info)
                    text += "زمان بین هر پست {} دقیقه ثبت شد.".format(mins)
                    update.reply_text(text=text.format(mins))
                    text, reply_markup = tabchi_info(tabchi_id)
                    msg: M
                    msg.edit_text(text=text, reply_markup=reply_markup)
                    new_psettins.pop(strid)
                else:
                    update.reply_text(text="لطفا فقط عدد انگلیسی وارد کنید، نمونه: 90\nبرای لغو عدد -1 را ارسال کنید")

    if new_gp_msgs.get(strid, None):
        tabchi_id, msg = new_gp_msgs[strid].values()
        if chiz_ersali == "0":
            mtd: M = update.reply_text(text="پروسه اضافه کردن محتوا به چت رندوم در گروه لغو شد، این پیام به طور خودکار پاک میشود.")
            new_gp_msgs.pop(strid)
        else:
            bot_info = get_bot_info(tabchi_id)
            bot_info["autochat_msgs"].append(chiz_ersali)
            save_bot_info(bot_info)
            text, reply_markup = tabchi_randmgp_tam(tabchi_id=tabchi_id)
            msg.edit_text(text=text, reply_markup=reply_markup)
            mtd: M = update.reply_text(text="محتوای ارسال شده به لیست پیام های رندوم گروه اضافه شد، این پیام به طور خودکار پاک میشود.")
            new_gp_msgs.pop(strid)
            event.wait(5)
        mtd.delete()

    if new_soaljvb.get(strid, None):
        tabchi_id, msg, status, Q, A, msg1 = new_soaljvb[strid].values()
        msg1: M
        msg: M
        if chiz_ersali == "0":
            new_soaljvb.pop(strid)
            update.reply_text(text="پروسه اضافه کردن سوال و جواب کنسل شد. چند لحظه بعد این پیام خود به خود پاک میشود.")
            t, r = tabchi_info(tabchi_id=tabchi_id)
            msg.edit_text(text=t, reply_markup=r)
        if Q is None:
            Q = chiz_ersali
            new_soaljvb[strid]["Q"] = Q
            m_: M = update.reply_text(text="متن *{}* به عنوان سوال ذخیره شد. حالا جواب مربوطه را ارسال کنید.".format(Q))
            new_soaljvb[strid]["msg1"] = m_
            return
        if A is None:
            A = chiz_ersali
            new_soaljvb[strid]["A"] = A
            bot_info = get_bot_info(tabchi_id)
            bot_info["assistant_data"][Q] = A
            save_bot_info(bot_info)
            new_soaljvb.pop(strid)
            t, r = tabchi_asstnt_tam(tabchi_id=tabchi_id)
            msg.edit_text(text=t, reply_markup=r)
            msg1.delete()
            return

    if update.text:
        text = update.text
        print("a1")
        if new_admin.get(strid, False):
            print("a2")
            tabchi_id, msg = new_admin[strid].values()
            bot_info = get_bot_info(tabchi_id)
            bot_admins = bot_info["admins"]
            if text.isdigit():
                print("a3")
                new_admin_id = int(text)
                if new_admin_id == 0:
                    print("a4")
                    mtd: M = update.reply_text(text="پروسه اضافه کردن ادمین لغو شد. این پیام پس از چند لحظه پاک خواهد شد.")
                    event.wait(5)
                    mtd.delete(revoke=True)
                    new_admin.pop(strid)
                    return
                if new_admin_id not in bot_admins:
                    print("a5")
                    if new_admin_id != Admin:
                        print("a6")
                        if new_admin_id != mainbot_info.id:
                            print("a7")
                            bot_info["admins"].append(new_admin_id)
                            save_bot_info(bot_info)
                            msg.delete()
                            update.reply_text(text="آیدی عددی {} به لیست ادمین ها اضافه شد.".format(text))
                            text, reply_markup = tabchi_info(tabchi_id=tabchi_id)
                            update.reply_text(text=text, reply_markup=reply_markup)
                            new_admin.pop(strid)
                        else:
                            update.reply_text(text="من که اصل کاری هستم {}، منظورت چیه؟".format(user.first_name))
                    else:
                        update.reply_text(text="تو که همین الانش هم ادمین اصلی هستی {} خودتو دست کم نگیر".format(user.first_name))
                else:
                    update.reply_text(text="آیدی عددی {} در حال حاضر در لیست ادمین ها وجود دارد.".format(text))
            else:
                update.reply_text(text="لطفا فقط آیدی عددی ادمین جدید را ارسال کنید.\nنمونه: `{}`".format(ManiJ))
        if user.id == new_tabchi.get("adder", None):
            if new_tabchi.get("status", None) == 1:
                if text.isdigit():
                    phone_number = f"+{text}"
                    password = None
                    try:
                        new_client = Client(name=phone_number[1:], api_id=api_id, api_hash=api_hash, proxy=proxy, password=password)
                    except:
                        update.reply_text(text="مجددا شماره را وارد کنید.")
                        return
                    print("created client")
                    new_client.connect()
                    print("client connected")

                    try:
                        code_sent: types.SentCode = new_client.send_code(phone_number)
                        update.reply_text(text="لطفا کد ارسال شده را وارد کنید.\n||در صورت اشتباه بودن شماره، دستور /cancel_bot را وارد کرده و از اول شروع کنید.||")
                    except Exception as E:
                        print(f"SEND CODE ERROR: {E}")
                        update.reply_text(text="خطایی در ارسال کد رخ داد، لطفا شماره {} خود را مجددا بررسی کرده و کمی بعد دوباره از طریق دکمه اقدام کنید.".format(phone_number))
                        new_client.disconnect()
                        return
                    new_tabchi["phone_number"] = phone_number
                    new_tabchi["client"] = new_client
                    new_tabchi["status"] = 2
                    new_tabchi["phone_code_hash"] = code_sent.phone_code_hash
                    return
                else:
                    update.reply_text(text=["لطفا شماره رو بدون + و با کد کشور مانند نمونه بنویسید.", "989120001111", "برای لغو عملیات از دستور /cancel_bot استفاده کنید."])
            if new_tabchi.get("status", None) == 2:
                if text.isdigit():
                    new_client: Client = new_tabchi["client"]
                    phone_number = new_tabchi["phone_number"]
                    phone_code_hash = new_tabchi["phone_code_hash"]

                    new_client.sign_in(phone_number=phone_number, phone_code=text, phone_code_hash=phone_code_hash)
                    about_tbch: types.User = new_client.get_me()
                    session_string = new_client.export_session_string()
                    new_client.send_message(chat_id="me", text="تبچی نصب شد!")
                    is_connected = new_client.is_connected
                    if is_connected:
                        new_client.disconnect()
                    """SAVE NEW TABCHI"""
                    bot_info = {
                        "id": about_tbch.id, "name": new_client.name, "date_created": jnowtime().timestamp(), "status": False,
                        "auto_pv": False, "auto_gp": False, "phone_number": phone_number, "username": about_tbch.first_name,
                        "mention": mention_maker(about_tbch.first_name, about_tbch.id), "admins": [], "pvs": [], "gps": [], "channels": [],
                        "posts": [], "last_post_sent": -1, "posts_settings": {"duration": 75, "send_at_once": False},
                        "joined_chats": [], "assistant_data": {}, "autochat_msgs": [], "session_string": session_string,
                        "first_msg": None, "auto_join_chats": False, "chats_to_join": [], "installed": False,
                        "auto_reaction": 10, "auto_message": 10
                    }
                    BOTS[str(about_tbch.id)] = new_client
                    save_bot_info(bot_info)
                    new_tabchi.clear()
                    update.reply_text(text="تبچی جدید اضافه و ذخیره شد!\nبرای نصب کامل تبچی، بات را یکبار /restart کنید\nحواستون باشه با این کار هم تبچی ها و هم ربات اصلی ری استارت میشن")


def get_system_information():
    memory = psutil.virtual_memory()
    memory_total = memory.total
    memory_used = memory.used
    memory_percent = memory.percent

    disk = psutil.disk_usage('/')
    disk_total = disk.total
    disk_used = disk.used
    disk_percent = disk.percent

    cpu_percent = psutil.cpu_percent()

    information = (f"🧭 Memory Usage:\n"
                   f"- Memory Total: {cbthrs(memory_total)}\n"
                   f"- Memory Used: {cbthrs(memory_used)}\n"
                   f"- Memory Percent: {memory_percent}%\n"
                   f"\n"
                   f"💿 Disk Usage:\n"
                   f"- Disk Total: {cbthrs(disk_total)}\n"
                   f"- Disk Used: {cbthrs(disk_used)}\n"
                   f"- Disk Percent: {disk_percent}%\n"
                   f"\n"
                   f"🔌 CPU Usage::\n"
                   f"- CPU Percent: {cpu_percent}%\n")

    return information


def random_true_false(percentage):
    return random.random() < (percentage / 100)


@bot.on_message(filters=filters.command(commands=["start", "help", "admins", main_command, "cancel_bot",
                                                  "restart", "resources"]), group=1)
def main_bot_handler1(client: Client, update: M):
    user = update.from_user
    command = update.command[0]
    admin_status = istadmin(user_id=user.id)

    if command in ["start", "help"]:
        update.reply_text(text=start_text)

    if command == main_command:
        msg: M = update.reply_text(text="در حال جمع آوری اطلاعات...")
        text, reply_markup = bots_info_list(user.id)
        msg.edit_text(text=text, reply_markup=reply_markup)

    if command in ["cancel_bot", "restart", "resources"]:
        if admin_status:
            if command == "resources":
                text = get_system_information()
                update.reply_text(text=text)
            if command == "cancel_bot":
                if admin_status == 1:
                    if len(new_tabchi) == 0:
                        update.reply_text(text="پروسه ای برای کنسل کردن موجود نیست.")
                    else:
                        new_tabchi.clear()
                        update.reply_text(text="پروسه اضافه کردن تبچی ریست شد، مجددا اقدام کنید.")
            if admin_status == 1 and command == "restart":
                PyFile_Restart()
    pass


def generate_random_tmp_filename(puffix="", suffix=None, length=8):
    # Generate a random string of letters and digits
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
    if suffix:
        random_string += "." + suffix.replace(".", "")
    return f"{puffix}{random_string}"


def add_members(client: Client, chat):
    members_list: list[types.User] = client.get_contacts()
    failed_members = 0
    done_members = 0
    add_report = {}
    members_ids = [x.id for x in members_list]
    chat_id = chat.id
    for member_id in members_ids:
        try:
            r = client.add_chat_members(chat_id=chat_id, user_ids=member_id)
        except:
            r = False
        add_report[str(member_id)] = btt(tof=r, true="✅", false="❌")
        if r:
            done_members += 1
        else:
            failed_members += 1
    filename = generate_random_tmp_filename(puffix="addmember_", suffix="json")
    with open(file=filename, mode="w") as addw:
        json.dump(add_report, addw, indent=2)

    text = ["⚙️ فایل آمار ادد های شما در گروه.",
            "میتوانید میزان موفقیت اد های انجام شده توسط تبچی {} برای گروه {} را مشاهده کنید.".format(client.me.id, chat_id)]
    return filename, text


def tabchi_handler(client: Client, update: M):
    me = client.me
    my_id = me.id
    tbot_info = get_bot_info(tbot_id=my_id)
    if not tbot_info["status"]:
        return

    user = update.from_user
    chat = update.chat
    if not user:
        return
    strid = str(user.id)

    """check if channel"""
    if chat.type == CHANNEL:
        if chat.id not in tbot_info["channels"]:
            tbot_info["channels"].append(chat.id)
            save_bot_info(tbot_json=tbot_info)

    """check if group"""
    if chat.type in [GROUP, SUPERGROUP]:
        if chat.id not in tbot_info["gps"]:
            tbot_info["gps"].append(chat.id)
            save_bot_info(tbot_json=tbot_info)
        if tbot_info["auto_gp"]:
            auto_reaction = tbot_info["auto_reaction"]
            auto_message = tbot_info["auto_message"]
            """send random message"""
            if random_true_false(auto_reaction):
                reaction = random.choice(chat.available_reactions.reactions)
                emoji = reaction.emoji
                update.react(emoji=emoji)
            if random_true_false(auto_message):
                chat_msgs = tbot_info["autochat_msgs"]
                if len(chat_msgs) != 0:
                    text = random.choice(chat_msgs)
                    update.reply_text(text)
        if update.text:
            command = update.text
            if command == f".addusers {my_id}":
                if istadmin(user_id=user.id, tbot_id=my_id):
                    permissions: types.ChatMember = client.get_chat_member(chat_id=chat.id, user_id=my_id)
                    if permissions.permissions.can_invite_users:
                        update.reply_text(text="در حال انجام عملیات.")
                        document, caption = add_members(client=client, chat=chat)
                        for uid in [user.id, Admin]:
                            bot.send_document(chat_id=uid, document=document, caption=caption)
                    else:
                        update.reply_text(text="من دسترسی این کار رو ندارم")

    if chat.type == PRIVATE and chat.id not in [777000]:
        first_time = False
        if not user.is_contact:
            client.add_contact(user_id=user.id, first_name=user.first_name)
        if user.id not in tbot_info["pvs"]:
            print(f"{user.id} not in pvs")
            tbot_info["pvs"].append(user.id)
            save_bot_info(tbot_json=tbot_info)
            tbot_info = get_bot_info(tbot_id=my_id)
            first_time = True
        if tbot_info["auto_pv"]:
            if first_time:
                first_msg = tbot_info["first_msg"]
                chat_id, msg_id, quote = first_msg.values()
                if first_msg:
                    tabchi_send_post(client=client, from_chat_id=chat_id, msg_id=msg_id, target_chat_id=chat.id, quote=quote)
            else:
                if update.text in tbot_info["assistant_data"]:
                    update.reply_text(text=tbot_info["assistant_data"][update.text])

    if new_broadcast.get(strid, None) and istadmin(tbot_id=my_id, user_id=user.id):
        if update.text:
            if update.text == "0":
                new_broadcast.pop(strid)
                update.reply_text(text="عملیات لغو شد.")
                return
        mgi = None
        if update.media_group_id:
            mgi = update.media_group_id
        if mgi:
            if mgi in new_broadcast[strid]["mgis"]:
                return
            new_broadcast[strid]["mgis"].append(mgi)
        tabchi_id = new_broadcast[strid]["tabchi_id"]
        """SAVE NEW BROADCAST"""
        broadcast = {"chat_id": update.chat.id, "msg_id": update.id, "quote": False,
                     "gps": True, "pvs": False}
        new_broadcast_data[str(tabchi_id)] = broadcast
        reply_markup = tabchi_broadcast_buttons(tabchi_id=tabchi_id)
        bot.send_message(chat_id=user.id, text="پنل تنظیمات پیام همگانی تبچی {}.\nدقت داشته باشید که پیام های همگانی به صورت موقت ذخیره میشوند.".format(tabchi_id), reply_markup=reply_markup)
    if new_post.get(strid, None) and istadmin(tbot_id=my_id, user_id=user.id):
        if update.text:
            if update.text == "0":
                new_post.pop(strid)
                update.reply_text(text="عملیات لغو شد.")
                return
        mgi = None
        if update.media_group_id:
            mgi = update.media_group_id
        if mgi:
            if mgi in new_post[strid]["mgis"]:
                return
            new_post[strid]["mgis"].append(mgi)
        tabchi_id = new_post[strid]["tabchi_id"]
        """SAVE NEW POST"""
        post = {"chat_id": update.chat.id, "msg_id": update.id, "quote": False,
                "gps": True, "pvs": False}
        bot_info = get_bot_info(tbot_id=tabchi_id)
        bot_info["posts"].append(post)
        save_bot_info(bot_info)
        msg: M = new_post[strid]["msg"]
        text, reply_markup = tabchi_posts_tam(tabchi_id=tabchi_id)

        msg.edit_text(text=text, reply_markup=reply_markup)
        update.reply_text(text="پست ذخیره شد! برای ادامه باقی کار ها از {} اقدام کنید.".format(mention_maker(name="بات اصلی", user_id=bot.me.id)))
        new_post.pop(strid)

    if new_first_msg.get(strid, None) and istadmin(tbot_id=my_id, user_id=user.id):
        if update.text:
            if update.text == "0":
                new_first_msg.pop(strid)
                update.reply_text(text="عملیات لغو شد.")
                return
        mgi = None
        if update.media_group_id:
            mgi = update.media_group_id
        if mgi:
            if mgi in new_post[strid]["mgis"]:
                return
            new_post[strid]["mgis"].append(mgi)
        tabchi_id = new_first_msg[strid]["tabchi_id"]
        """SAVE NEW FIRST MSG"""
        first_msg = {"chat_id": update.chat.id, "msg_id": update.id, "quote": False}
        bot_info = get_bot_info(tbot_id=tabchi_id)
        bot_info["first_msg"] = first_msg
        save_bot_info(bot_info)
        msg: M = new_first_msg[strid]["msg"]
        text, reply_markup = tabchi_info(tabchi_id=tabchi_id)
        msg.edit_text(text=text, reply_markup=reply_markup)
        update.reply_text(text="پیام ذخیره شد! برای ادامه باقی کار ها از {} اقدام کنید.".format(mention_maker(name="بات اصلی", user_id=bot.me.id)))
        new_first_msg.pop(strid)


    if tbot_info["auto_join_chats"]:
        urls = get_string_urls(message=update)
        join_chats(client=client, urls=urls, time_to_wait=45)

    if update.text:
        if update.text == ".checkifonline":
            update.reply_text(text=".")

    pass


new_tabchi = {}
new_admin = {}
new_post = {}
new_psettins = {}
new_soaljvb = {}
new_gp_msgs = {}
new_gp = {}
new_leave = {}
new_first_msg = {}
new_auto_message = {}
new_auto_reaction = {}
new_broadcast = {}
new_broadcast_data = {}



def tabchi_buttons(tabchi_id):
    bot_info = get_bot_info(tabchi_id)
    status = bot_info["status"]
    auto_pv = bot_info["auto_pv"]
    auto_gp = bot_info["auto_gp"]
    auto_join = bot_info["auto_join_chats"]
    status_text = btt(status)
    auto_pv_text = btt(auto_pv, "فعال🟢", "غیرفعال⚫️")
    auto_gp_text = btt(auto_gp, "فعال🟢", "غیرفعال⚫️")
    auto_join_text = btt(auto_join, "فعال🟢", "غیرفعال⚫️")

    reply_markup = IKM([
        [
            IKB(text="👤ادمین های بات", callback_data=f"tabchi_admins_{tabchi_id}"),
            IKB(text="وضعیت: {}".format(status_text), callback_data=f"tabchi_status_{tabchi_id}"),
        ],
        [
            IKB(text="منشی: {}".format(auto_pv_text), callback_data=f"tabchi_auto_pv_{tabchi_id}"),
            IKB(text="چت گروه: {}".format(auto_gp_text), callback_data=f"tabchi_auto_gp_{tabchi_id}"),
         ],
        [
            IKB(text="تنظیمات پیام اولیه 🔖", callback_data=f"tabchi_first_msg_{tabchi_id}")
        ],
        [
            IKB(text="ارسال پست همگانی", callback_data=f"tabchi_broadcast_panel_{tabchi_id}"),
            IKB(text="⚙️ تنظیمات چت خودکار", callback_data=f"tabchi_chatsettings_{tabchi_id}")
        ],
        [
            IKB(text="عضو جهت تبلیغات", callback_data=f"tabchi_join_gps_{tabchi_id}"),
            IKB(text="عضو جهت جذب پیوی", callback_data=f"tabchi_join_pvs_{tabchi_id}"),
        ],
        [
            IKB(text="جوین خودکار: {}".format(auto_join_text), callback_data=f"tabchi_auto_join_{tabchi_id}"),
        ],
        [
            IKB(text="جوین با لینک".format(auto_join_text), callback_data=f"tabchi_join_link_{tabchi_id}"),
            IKB(text="خروج از چت ها".format(auto_join_text), callback_data=f"tabchi_Lchats_{tabchi_id}"),
        ],
        [
            IKB(text="اطلاعات منشی هوشمند👩‍💻", callback_data=f"tabchi_assistant_{tabchi_id}"),
        ],
        [
            IKB(text="پیام های چت در گروه📗", callback_data=f"tabchi_gpmsgs_{tabchi_id}"),
        ],
        [
            IKB(text="تنظیمات پست ها⚙️", callback_data=f"tabchi_psettings_{tabchi_id}"),
            IKB(text="پست های تبچی📝", callback_data=f"tabchi_posts_{tabchi_id}"),
        ],
        [
            IKB(text="به روز رسانی🔄", callback_data=f"tabchi_uppanel_{tabchi_id}")
        ],
        [
            IKB(text="ℹ️ راهنمای اد زدن ممبر", callback_data=f"tabchi_add_help_{tabchi_id}")
        ],
        [
            IKB(text="❌حذف تبچی🗑", callback_data=f"tabchi_delete_{tabchi_id}"),
            IKB(text="❌حذف تبچی🗑", callback_data=f"tabchi_delete_{tabchi_id}")
        ],
        [
            IKB(text="بازگشت به لیست تبچی ها🔙", callback_data="tabchi_list")
        ],
    ])
    return reply_markup


def tabchi_info_text(tabchi_id):
    bot_info: dict = get_bot_info(tabchi_id)
    tid = int(tabchi_id)
    date_created = bot_info["date_created"]
    status = bot_info["status"]
    auto_pv = bot_info["auto_pv"]
    auto_gp = bot_info["auto_gp"]
    phone_number = bot_info["phone_number"]
    username = bot_info["username"]
    pvs = bot_info["pvs"]
    gps = bot_info["gps"]
    channels = bot_info["channels"]

    date_created = date_from_timestamp(date_created, start_fmt)
    status = btt(status)
    auto_pv = btt(auto_pv, "فعال👍", "غیرفعال😴")
    auto_gp = btt(auto_gp, "فعال🤳", "غیرفعال🤫")
    text = ((
                "مشخصات تبچی {name} با آیدی عددی {tid}\n\n"
                "🧩شماره تبچی: {phone_number}\n"
                "⏰زمان ساخت: {date_created}\n"
                "تعداد پیوی ها: {pvs}\n"
                "تعداد گروه ها: {gps}\n"
                "تعداد کانال ها: {channels}\n"
                "🔋وضعیت: {status}\n\n"
                "👩‍💻منشی: {auto_pv}\n"
                "💌چت در گروه: {auto_gp}\n"
            )
            .format(name=username, tid=tid, phone_number=phone_number, date_created=date_created, channels=REWPN(len(channels)),
                    status=status, auto_pv=auto_pv, auto_gp=auto_gp, pvs=REWPN(len(pvs)), gps=REWPN(len(gps))))
    return text


def tabchi_info(tabchi_id):
    text = tabchi_info_text(tabchi_id=tabchi_id)
    reply_markup = tabchi_buttons(tabchi_id=tabchi_id)
    return text, reply_markup


def tabchi_admins_tam(tabchi_id):
    bot_info: dict = get_bot_info(tabchi_id)
    admins = bot_info["admins"]
    if len(admins) == 0:
        text = "در حال حاضر ادمینی غیر از شما برای بات تعریف نشده"
    else:
        text = "ادمین های بات به شرح زیر میباشند.\nبرای حذف هر ادمین، روی دکمه‌ی مربوطه کلیک کنید."
    buttons = []
    for admin in admins:
        tta = IKB(text="🗑 حذف ادمین {}".format(admin), callback_data=f"tabchi_removeadmin_{tabchi_id}_{admin}")
        buttons.append(tta)
    buttons = slice_into_pairs(buttons)
    add_btn = IKB(text="افزودن ادمین➕", callback_data=f"tabchi_addadmin_{tabchi_id}")
    bck_btn = IKB(text="بازگشت🔙", callback_data=f"tabchi_panel_{tabchi_id}")
    buttons.append([bck_btn, add_btn])
    return text, IKM(buttons)


def tabchi_posts_tam(tabchi_id):
    bot_info = get_bot_info(tabchi_id)
    posts = bot_info["posts"]
    if len(posts) == 0:
        text = "در حال حاضر پستی برای این تبچی ثبت نشده!"
    else:
        text = "پست های تبچی به شرح زیر میباشند.\nبرای مدیریت هر پست، روی دکمه‌ی مربوطه کلیک کنید."
    buttons = []
    for post_index in range(len(posts)):
        post = posts[post_index]
        _, _, quote, gps, pvs = post.values()
        quote = btt(tof=quote)
        gps = btt(tof=gps, true="✅", false="❌")
        pvs = btt(tof=pvs, true="✅", false="❌")
        post_index = str(post_index + 1)
        tta = [
            IKB(text="نقل قول {}: {}".format(post_index, quote), callback_data=f"tabchi_qpost_{tabchi_id}_{post_index}"),
            IKB(text="باز بینی پست {}".format(post_index), callback_data=f"tabchi_prvpost_{tabchi_id}_{post_index}"),
        ]
        buttons.append(tta)
        tta = [
            IKB(text="ارسال به پیوی: {}".format(pvs), callback_data=f"tabchi_pvs_post_{tabchi_id}_{post_index}"),
            IKB(text="ارسال به گروه: {}".format(gps), callback_data=f"tabchi_gps_post_{tabchi_id}_{post_index}"),
        ]
        buttons.append(tta)
        tta = [IKB(text="🗑حذف پست {}".format(post_index), callback_data=f"tabchi_removepost_{tabchi_id}_{post_index}")]
        buttons.append(tta)

    add_btn = IKB(text="افزودن پست➕", callback_data=f"tabchi_addpost_{tabchi_id}")
    bck_btn = IKB(text="بازگشت🔙", callback_data=f"tabchi_panel_{tabchi_id}")
    buttons.append([bck_btn, add_btn])
    reply_markup = IKM(buttons)
    return text, reply_markup


def tabchi_asstnt_tam(tabchi_id):
    bot_info = get_bot_info(tabchi_id)
    assistant_data: dict = bot_info["assistant_data"]
    if len(assistant_data) == 0:
        text = ["در حال حاضر جواب خودکاری برای منشی هوشمند ثبت نشده."]
    else:
        text = ["لیست سوالات و جواب های منشی هوشمند به شرح زیر میباشد:\n"]
    buttons = []
    i = 1
    for q in assistant_data:
        a = assistant_data[q]
        tta = "{}. سوال: {}\nجواب: {}".format(i, q, a)
        text.append(tta)

        bta = IKB(text="🗑حذف مورد {}".format(i), callback_data="tabchi_removeqaa_{}_{}".format(tabchi_id, i))
        buttons.append(bta)
        i += 1
    text = "\n".join(text)
    buttons = slice_into_pairs(buttons, 3)
    add_btn = IKB(text="➕افزودن سوال و جواب", callback_data=f"tabchi_addqaa_{tabchi_id}")
    bck_btn = IKB(text="بازگشت🔙", callback_data=f"tabchi_panel_{tabchi_id}")
    buttons.append([bck_btn, add_btn])
    return text, IKM(buttons)


def tabchi_randmgp_tam(tabchi_id):
    bot_info: dict = get_bot_info(tabchi_id)
    random_msgs = bot_info["autochat_msgs"]
    if len(random_msgs) == 0:
        text = "در حال حاضر پیام/محتوایی برای ارسال رندوم در گروه ها ثبت نشده."
    else:
        text = "پیام/محتوا ها برای ارسال رندوم به شرح زیر است:\n\n"
    buttons = []
    i = 1
    """
    IKB(text="بازبینی محتوا", callback_data=f"prviw_{random_msg}")
    """
    for random_msg in random_msgs:
        tta = [
            IKB(text="بازبینی محتوا👀", callback_data=f"tabchi_prviw_{tabchi_id}_{i}"),
            IKB(text="🗑حذف مورد {}".format(i), callback_data="tabchi_removerandomsg_{}_{}".format(tabchi_id, i)),
        ]
        text += f"{i}. {random_msg}\n"
        buttons.append(tta)

    add_btn = IKB(text="➕افزودن پیام/محتوا", callback_data=f"tabchi_addrandomsg_{tabchi_id}")
    bck_btn = IKB(text="بازگشت🔙", callback_data=f"tabchi_panel_{tabchi_id}")
    buttons.append([bck_btn, add_btn])
    return text, IKM(buttons)


def tabchi_psettings(tabchi_id):
    bot_info: dict = get_bot_info(tabchi_id)
    duration, send_at_once = bot_info["posts_settings"].values()
    text = "برای ویرایش هر بخش روی آن ضربه بزنید."
    send_at_once = btt(send_at_once)
    reply_markup = IKM([
        [
            IKB(text="زمان بین هر پست: {}".format(duration), callback_data=f"tabchi_pduration_{tabchi_id}"),
        ],
        [
            IKB(text="ارسال همزمان پست ها: {}".format(send_at_once), callback_data=f"tabchi_psao_{tabchi_id}")
        ],
        [
            IKB(text="بازگشت🔙", callback_data=f"tabchi_panel_{tabchi_id}")
        ]
                        ])
    return text, reply_markup


def tabchi_first_msg(tabchi_id):
    bot_info: dict = get_bot_info(tabchi_id)
    buttons = []
    if bot_info["first_msg"]:
        text = "از گزینه های زیر انتخاب کنید."
        buttons.append([IKB(text="👀 بازبینی پیام اولیه", callback_data=f"tabchi_prv_first_msg_{tabchi_id}")])
        buttons.append([IKB(text="حذف پیام اولیه ❌", callback_data=f"tabchi_del_first_msg_{tabchi_id}")])
    else:
        text = "پیامی برای این بخش ثبت نشده"
    tta = [
        IKB(text="تنظیم پیام جدید 🆕", callback_data=f"tabchi_set_first_msg_{tabchi_id}"),
        IKB(text="بازگشت 🔙", callback_data=f"tabchi_panel_{tabchi_id}")
          ]
    buttons.append(tta)
    reply_markup = IKM(buttons)
    return text, reply_markup


def tabchi_broadcast_starter(update, tabchi_id):
    chat_id, msg_id, quote, gps, pvs = new_broadcast_data[tabchi_id].values()
    bot_info = get_bot_info(tbot_id=tabchi_id)
    chat_ids = []
    if gps or pvs:
        if gps:
            chat_ids.extend(bot_info["gps"])
        if pvs:
            chat_ids.extend(bot_info["pvs"])
        if len(chat_ids):
            tbot = get_tclient(bot_id=tabchi_id)
            update.edit_message_text(text="پروسه ارسال پیام همگانی آغاز شد.")
            new_broadcast_data.pop(tabchi_id)
            for target_id in chat_ids:
                try:
                    tabchi_send_post(client=tbot, from_chat_id=chat_id, msg_id=msg_id, target_chat_id=target_id, quote=quote)
                    time.sleep(15)
                except:
                    pass
            update.edit_message_text(text="پروسه ارسال پیام همگانی به اتمام رسید.")
        else:
            update.answer(text="چتی برای ارسال پیام یافت نشد! تنظیمات را بازبینی کنید.")
    else:
        update.answer(text="چتی برای ارسال پیام یافت نشد! تنظیمات را بازبینی کنید.")
    pass


def tabchi_broadcast_buttons(tabchi_id):
    broadcast_data = new_broadcast_data.get(tabchi_id, None)
    if broadcast_data:
        chat_id, msg_id, quote, gps, pvs = broadcast_data.values()
        reply_markup = IKM([
            [
                IKB(text="نقل قول: {}".format(btt(quote)), callback_data=f"tabchi_broadcast_quote_{tabchi_id}"),
                IKB(text="بازبینی", callback_data=f"tabchi_broadcast_preview_{tabchi_id}")
            ],
            [
                IKB(text="ارسال به پیوی: {}".format(btt(pvs, "فعال🟢", "غیرفعال⚫️")), callback_data=f"tabchi_broadcast_pvs_{tabchi_id}"),
                IKB(text="ارسال به گروه: {}".format(btt(gps, "فعال🟢", "غیرفعال⚫️")), callback_data=f"tabchi_broadcast_gps_{tabchi_id}")
            ],
            [
                IKB(text="ارسال پیام همگانی", callback_data=f"tabchi_broadcast_start_{tabchi_id}")
            ],
            [
                IKB(text="لغو عملیات", callback_data=f"tabchi_broadcast_pop_{tabchi_id}")
            ]
        ])
        return reply_markup
    else:
        return False


def msg_type(msg: M):
    if msg.document:
        return IMD, msg.document.file_id, msg.caption, msg.caption_entities
    elif msg.photo:
        return IMP, msg.photo.file_id, msg.caption, msg.caption_entities
    elif msg.video:
        return IMV, msg.video.file_id, msg.caption, msg.caption_entities
    elif msg.animation:
        return IMAN, msg.animation.file_id, msg.caption, msg.caption_entities
    elif msg.audio:
        return IMAU, msg.audio.file_id, msg.caption, msg.caption_entities
    elif msg.video_note:
        return "video_note", msg.video_note.file_id, None, None
    elif msg.voice:
        return "voice", msg.voice.file_id, msg.caption, msg.caption_entities
    else:
        return "text", "", "", msg.entities


def save_msg_in_json(msgs: list[M]):
    msgs_jdata = []
    for msg in msgs:
        type_, file_id, caption, entities = msg_type(msg)
        msg_data = {"type": type_, "content": file_id, "caption": caption, "entities": entities}
        msgs_jdata.append(msg_data)
    posts_data = {"medias": msgs_jdata, "quote": True}
    return msgs_jdata


@bot.on_callback_query(group=2)
def call_back_handler(client, update: types.CallbackQuery):
    call_data = update.data
    print(f"call_data: {call_data}")
    clicked_user = update.from_user
    """
    tabchi_jid = call_data[len("tabchi_panel_"):]
    bot_info = get_bot_info(tabchi_jid)
    """
    if call_data.startswith("tabchi_panel_"):
        tabchi_jid = call_data[len("tabchi_panel_"):]
        if istadmin(user_id=clicked_user.id, tbot_id=tabchi_jid):
            text, reply_markup = tabchi_info(tabchi_id=tabchi_jid)
            update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_uppanel_"):
        tabchi_jid = call_data[len("tabchi_uppanel_"):]
        text, reply_markup = tabchi_info(tabchi_id=tabchi_jid)
        try:
            update.edit_message_text(text=text, reply_markup=reply_markup)
        except:
            pass
        update.answer(text="پنل به روز رسانی شد.")

    if call_data == "tabchi_list":
        text, reply_markup = bots_info_list(clicked_user.id)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_admins_"):
        tabchi_jid = call_data[len("tabchi_admins_"):]
        adminstatus = istadmin(tbot_id=tabchi_jid, user_id=clicked_user.id)
        if adminstatus == 1:
            text, reply_markup = tabchi_admins_tam(tabchi_jid)
            update.edit_message_text(text=text, reply_markup=reply_markup)
        else:
            update.answer(text="شما به این بخش دسترسی ندارید. برو خونتون", show_alert=True)

    if call_data.startswith("tabchi_addadmin_"):
        tabchi_jid = call_data[len("tabchi_addadmin_"):]
        adminstatus = istadmin(tbot_id=tabchi_jid, user_id=clicked_user.id)
        if adminstatus == 1:
            new_admin[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "msg": update.message}
            update.answer(text="لطفا آیدی عددی ادمین تبچی را بفرستید. در صورت انصراف عدد 0 را ارسال کنید", show_alert=True)
        else:
            update.answer(text="شما به این بخش دسترسی ندارید.")

    if call_data.startswith("tabchi_removeadmin_"):
        tabchi_jid, admin_id = call_data[len("tabchi_removeadmin_"):].split("_")
        bot_info = get_bot_info(tabchi_jid)
        bot_info["admins"].remove(int(admin_id))
        save_bot_info(bot_info)
        update.answer(text="ادمین {} از لیست ادمین های تبچی {} حذف شد.".format(admin_id, tabchi_jid))
        text, reply_markup = tabchi_admins_tam(tabchi_id=tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith(("tabchi_status_", "tabchi_auto_gp_", "tabchi_auto_pv_", "tabchi_auto_join_")):
        if call_data.startswith("tabchi_status_"):
            key, lenk = "status", "tabchi_status_"
        if call_data.startswith("tabchi_auto_gp_"):
            key, lenk = "auto_gp", "tabchi_auto_gp_"
        if call_data.startswith("tabchi_auto_pv_"):
            key, lenk = "auto_pv", "tabchi_auto_pv_"
        if call_data.startswith("tabchi_auto_join_"):
            key, lenk = "auto_join_chats", "tabchi_auto_join_"
        tabchi_jid = call_data[len(lenk):]
        bot_info = get_bot_info(tabchi_jid)
        status = bot_info[key]
        bot_info[key] = inverseb(status)
        save_bot_info(bot_info)
        text, reply_markup = tabchi_info(tabchi_id=tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)
        update.answer(text="تغییرات اعمال شد.")

    if call_data.startswith("tabchi_assistant_"):
        tabchi_jid = call_data[len("tabchi_assistant_"):]
        text, reply_markup = tabchi_asstnt_tam(tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_addqaa_"):
        tabchi_jid = call_data[len("tabchi_addqaa_"):]
        adminstatus = istadmin(tbot_id=tabchi_jid, user_id=clicked_user.id)
        if adminstatus:
            new_soaljvb[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "msg": update.message,
                                                 "status": 1, "Q": None, "A": None,
                                                 "msg1": None}
            update.edit_message_text(text="لطفا ابتدا سوال (متن کاربر) را وارد کنید.\nدر صورت انصراف در هر مرحله، عدد 0 را ارسال کنید.")
        else:
            update.answer(text="شما به این بخش دسترسی ندارید.")

    if call_data.startswith("tabchi_removeqaa_"):
        tabchi_jid, num = call_data[len("tabchi_removeqaa_"):].split("_")
        bot_info = get_bot_info(tabchi_jid)
        soaljvbs = bot_info["assistant_data"]
        key = list(soaljvbs.keys())[int(num)-1]
        soaljvbs.pop(key)
        bot_info["assistant_data"] = soaljvbs
        save_bot_info(bot_info)
        update.answer(text="مورد {} حذف شد.".format(num), show_alert=True)
        t, r = tabchi_asstnt_tam(tabchi_id=tabchi_jid)
        update.edit_message_text(text=t, reply_markup=r)

    if call_data.startswith("tabchi_gpmsgs_"):
        tabchi_jid = call_data[len("tabchi_gpmsgs_"):]
        text, reply_markup = tabchi_randmgp_tam(tabchi_id=tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_addrandomsg_"):
        tabchi_jid = call_data[len("tabchi_addrandomsg_"):]
        new_gp_msgs[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "msg": update.message}
        update.answer(text="پیام، استیکر، گیف یا هرچی که میخوای ربات رندوم تو گروه ها ارسال کنه بفرست. برای لغو عدد 0 رو ارسال کن.")

    if call_data.startswith("tabchi_removerandomsg_"):
        tabchi_jid, num = call_data[len("tabchi_removerandomsg_"):].split("_")
        bot_info = get_bot_info(tabchi_jid)
        del bot_info["autochat_msgs"][int(num)-1]
        save_bot_info(bot_info)
        update.answer(text="مورد {} حذف شد.".format(num), show_alert=True)
        text, reply_markup = tabchi_randmgp_tam(tabchi_id=tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_prviw_"):
        tabchi_jid, num = call_data[len("tabchi_prviw_"):].split("_")
        bot_info = get_bot_info(tabchi_jid)
        tofid = bot_info["autochat_msgs"][int(num)-1]
        try:
            try:
                tmsg: M = update.message.reply_cached_media(file_id=tofid)
                tmsg.reply_text(text=REWPN("محتوای شماره {}:".format(num)), quote=True)
            except:
                tmsg: M = update.message.reply_text(text=tofid)
                tmsg.reply_text(text=REWPN("محتوای شماره {}:".format(num)), quote=True)
            update.answer(text="محتوا برای بازبینی ارسال شد.")
        except:
            update.answer(text="این محتوا مشکل داشته و از لیست حذف میشود.")
            bot_info = get_bot_info(tabchi_jid)
            del bot_info["autochat_msgs"][int(num) - 1]
            save_bot_info(bot_info)
            text, reply_markup = tabchi_randmgp_tam(tabchi_id=tabchi_jid)
            update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_delete_"):
        tabchi_jid = call_data[len("tabchi_delete_"):]
        adminstatus = istadmin(user_id=clicked_user.id, tbot_id=tabchi_jid)
        if adminstatus == 1:
            bot_info = get_bot_info(tabchi_jid)
            bot_name = bot_info["name"]
            jsonpath = os.path.join(Tbots_dir, f"TBOT-{tabchi_jid}.json")
            sshnpath = f"{bot_name}.session"
            media_grp = [
                IMD(media=jsonpath, caption=jsonpath),
                IMD(media=sshnpath, caption=sshnpath)
                        ]
            update.message.reply_media_group(media=media_grp)
            os.remove(jsonpath)
            os.remove(sshnpath)
            BOTS.pop(tabchi_jid)
            text, reply_markup = bots_info_list(clicked_user.id)
            update.answer(text="تبچی حذف شد.\nبرای حذف کامل تبچی، یک بار /restart کنید.", show_alert=True)
            update.edit_message_text(text=text, reply_markup=reply_markup)
        else:
            update.answer(text="شما به این بخش دسترسی ندارید.", show_alert=True)

    if call_data.startswith("tabchi_posts_"):
        tabchi_jid = call_data[len("tabchi_posts_"):]
        text, reply_markup = tabchi_posts_tam(tabchi_id=tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_addpost_"):
        tabchi_jid = call_data[len("tabchi_addpost_"):]
        tbot: Client = get_tclient(bot_id=tabchi_jid)
        try:
            tbot.start()
        except:
            pass
        tbot.send_message(chat_id=clicked_user.id, text="پستی که میخواید رو برای من بفرستید.")

        new_post[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "status": 1, "mgis": [], "msg": update.message}
        update.answer(text="لطفا پست رو به پیوی تبچی ارسال کنید، برای لغو عدد 0 رو به تبچی مربوطه بفرستید.", show_alert=True)

    if call_data.startswith("tabchi_removepost_"):
        tabchi_jid, post_id = call_data[len("tabchi_removepost_"):].split("_")
        bot_info = get_bot_info(tbot_id=tabchi_jid)
        bot_info["posts"].pop(int(post_id) - 1)
        save_bot_info(bot_info)
        text, reply_markup = tabchi_posts_tam(tabchi_id=tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_prvpost_"):
        tabchi_jid, post_id = call_data[len("tabchi_prvpost_"):].split("_")
        post_id = int(post_id) - 1
        bot_info = get_bot_info(tbot_id=tabchi_jid)
        post_data = bot_info["posts"][post_id]
        chat_id, msg_id, quote, _, _ = post_data.values()
        client = get_tclient(bot_id=tabchi_jid)
        tabchi_send_post(client=client, from_chat_id=chat_id, msg_id=msg_id, target_chat_id=update.message.chat.id, quote=quote)
        update.answer(text="بازبینی پست توسط ربات تبچی ارسال شد.", show_alert=True)

    if call_data.startswith("tabchi_qpost_"):
        tabchi_jid, post_id = call_data[len("tabchi_qpost_"):].split("_")
        bot_info = get_bot_info(tabchi_jid)
        post_id = int(post_id) - 1
        val = bot_info["posts"][post_id]["quote"]
        val = inverseb(val)
        bot_info["posts"][post_id]["quote"] = val
        save_bot_info(bot_info)
        text, reply_markup = tabchi_posts_tam(tabchi_id=tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_psettings_"):
        tabchi_jid = call_data[len("tabchi_psettings_"):]
        text, reply_markup = tabchi_psettings(tabchi_id=tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_pduration_"):
        tabchi_jid = call_data[len("tabchi_pduration_"):]
        new_psettins[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "msg": update.message}
        update.answer(text="لطفا مدت زمان بین هر پست را به دقیقه و انگلیسی ارسال کنید، برای لغو عملیات عدد -1 را وارد کنید.")

    if call_data.startswith("tabchi_psao_"):
        tabchi_jid = call_data[len("tabchi_psao_"):]
        bot_info = get_bot_info(tabchi_jid)
        val = bot_info["posts_settings"]["send_at_once"]
        val = inverseb(val)
        bot_info["posts_settings"]["send_at_once"] = val
        save_bot_info(bot_info)
        text, reply_markup = tabchi_psettings(tabchi_id=tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_join_link_"):
        tabchi_jid = call_data[len("tabchi_join_link_"):]
        new_gp[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "msg": update.message}
        update.answer(text="لطفا لینک یا آیدی گروه رو ارسال و برای لغو عدد -1 رو ارسال کنید.")

    if call_data.startswith("tabchi_Lchats_"):
        tabchi_jid = call_data[len("tabchi_Lchats_"):]
        reply_markup = IKM([
            [
                IKB(text="خروج از گروه ها به تعداد", callback_data=f"tabchi_leave_gps_{tabchi_jid}"),
            ],
            [
                IKB(text="خروج از کانال ها به تعداد", callback_data=f"tabchi_leave_channels_{tabchi_jid}")
            ],
            [
                IKB(text="بازگشت🔙", callback_data=f"tabchi_panel_{tabchi_jid}")
            ]
                            ])
        update.edit_message_text(text="از گزینه های زیر انتخاب کنید.", reply_markup=reply_markup)

    if call_data.startswith("tabchi_leave_"):
        typee, tabchi_jid = call_data[len("tabchi_leave_"):].split("_")
        new_leave[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "chat_type": typee}
        chttype = {"channels": "کانال ها", "gps": "گروه ها"}
        text = "تعداد {}یی که میخواید تبچی از اون ها لفت بده رو ارسال کنید، برای لغو عدد 0 رو ارسال کنید.".format(chttype[typee])
        update.answer(text=text, show_alert=True)

    if call_data.startswith("tabchi_first_msg_"):
        tabchi_jid = call_data[len("tabchi_first_msg_"):]
        text, reply_markup = tabchi_first_msg(tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_set_first_msg_"):
        tabchi_jid = call_data[len("tabchi_set_first_msg_"):]
        tbot: Client = get_tclient(bot_id=tabchi_jid)
        tbot.send_message(chat_id=clicked_user.id, text="پیام مورد نظر رو برای من بفرستید.")
        new_first_msg[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "status": 1, "mgis": [], "msg": update.message}
        update.answer(text="لطفا پیام جدید رو به پیوی تبچی ارسال کنید، برای لغو عدد 0 رو به تبچی مربوطه بفرستید.", show_alert=True)

    if call_data.startswith("tabchi_prv_first_msg_"):
        tabchi_jid = call_data[len("tabchi_prv_first_msg_"):]
        bot_info = get_bot_info(tbot_id=tabchi_jid)
        first_msg_data = bot_info["first_msg"]
        chat_id, msg_id, quote = first_msg_data.values()
        client = get_tclient(bot_id=tabchi_jid)
        tabchi_send_post(client=client, from_chat_id=chat_id, msg_id=msg_id, target_chat_id=update.message.chat.id, quote=quote)
        update.answer(text="بازبینی پیام توسط ربات تبچی ارسال شد.", show_alert=True)

    if call_data.startswith("tabchi_del_first_msg_"):
        tabchi_jid = call_data[len("tabchi_del_first_msg_"):]
        bot_info = get_bot_info(tbot_id=tabchi_jid)
        bot_info["first_msg"] = None
        save_bot_info(bot_info)
        text, reply_markup = tabchi_first_msg(tabchi_jid)
        update.answer(text="پیام حذف شد.")
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith(("tabchi_pvs_post_", "tabchi_gps_post_")):
        _, typee, _, tabchi_jid, post_id = call_data.split("_")
        post_id = int(post_id) - 1
        bot_info = get_bot_info(tbot_id=tabchi_jid)
        val_data = bot_info["posts"][post_id][typee]
        bot_info["posts"][post_id][typee] = inverseb(tof=val_data)
        save_bot_info(bot_info)
        text, reply_markup = tabchi_posts_tam(tabchi_id=tabchi_jid)
        update.edit_message_text(text=text, reply_markup=reply_markup)

    if call_data.startswith("tabchi_add_help_"):
        tabchi_jid = call_data[len("tabchi_add_help_"):]
        text = ["برای اد زدن ممبر به گروه، ابتدا تبچی رو عضو گروه کنید و دسترسی عضو کردن افراد رو فعال کنید، سپس دستور زیر رو در گروه وارد کنید.",
                f".addusers {tabchi_jid}"]
        update.message.reply_text(text="\n\n".join(text))

    if call_data.startswith("tabchi_join_"):
        typee, tabchi_jid = call_data[len("tabchi_join_"):].split("_")
        urls = {"pvs": chats_to_join, "gps": gps_to_join}[typee]
        tbot = get_tclient(bot_id=tabchi_jid)
        update.answer(text="پروسه عضو شدن آغاز شد.", show_alert=True)
        join_chats(client=tbot, urls=urls, time_to_wait=240)

    if call_data.startswith("tabchi_chatsettings_"):
        tabchi_jid = call_data[len("tabchi_chatsettings_"):]
        bot_info = get_bot_info(tbot_id=tabchi_jid)
        auto_reaction = bot_info["auto_reaction"]
        auto_message = bot_info["auto_message"]
        bck_btn = IKB(text="بازگشت🔙", callback_data=f"tabchi_panel_{tabchi_jid}")

        text = "شدت ارسال پیام خودکار: {}%\nشدت ارسال ری‌اکشن خودکار: {}%".format(auto_message, auto_reaction)
        reply_markup = IKM([
                    [IKB(text="تنظیم شدت ارسال پیام خودکار", callback_data=f"tabchi_set_auto_message_{tabchi_jid}")],
                    [IKB(text="تنظیم شدت ری‌اکشن خودکار", callback_data=f"tabchi_set_auto_reaction_{tabchi_jid}")],
                    [bck_btn]
                            ])
        update.message.edit_text(text=text, reply_markup=reply_markup)

    if call_data.startswith(("tabchi_set_auto_message_", "tabchi_set_auto_reaction_")):
        cd = call_data.split("_")
        mode = f"auto_{cd[3]}"
        tabchi_jid = cd[-1]
        if mode == "auto_message":
            text = "پیام"
            new_auto_message[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "msg": update.message}
        if mode == "auto_reaction":
            text = "ری‌اکشن"
            new_auto_reaction[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "msg": update.message}
        update.answer(text="برای تنظیم شدت ارسال {} یک عدد بین 0 تا 100 ارسال کنید. برای لغو عدد -1 رو ارسال کنید.".format(text))

    if call_data.startswith("tabchi_broadcast_panel_"):
        tabchi_jid = call_data[len("tabchi_broadcast_panel_"):]
        tbot: Client = get_tclient(bot_id=tabchi_jid)
        tbot.send_message(chat_id=clicked_user.id, text="پستی که میخواید رو برای من بفرستید.")
        update.answer(text="لطفا پست رو به پیوی تبچی ارسال کنید، برای لغو عدد 0 رو به تبچی مربوطه بفرستید.", show_alert=True)
        new_broadcast[str(clicked_user.id)] = {"tabchi_id": tabchi_jid, "status": 1, "mgis": [], "msg": update.message}
        return

    if call_data.startswith("tabchi_broadcast_"):
        """quote", "gps", "pvs"""
        _, _, mode, tabchi_jid = call_data.split("_")
        if mode in ["quote", "gps", "pvs"]:
            chat_id, msg_id, quote, gps, pvs = new_broadcast_data[tabchi_jid].values()
            if mode == "quote":
                new_data = inverseb(quote)
            if mode == "gps":
                new_data = inverseb(gps)
            if mode == "pvs":
                new_data = inverseb(pvs)
            new_broadcast_data[tabchi_jid][mode] = new_data
            reply_markup = tabchi_broadcast_buttons(tabchi_id=tabchi_jid)
            update.edit_message_reply_markup(reply_markup=reply_markup)

    if call_data.startswith("tabchi_broadcast_preview_"):
        tabchi_jid = call_data[len("tabchi_broadcast_preview_"):]
        chat_id, msg_id, quote, gps, pvs = new_broadcast_data[tabchi_jid].values()
        tbot = get_tclient(bot_id=tabchi_jid)
        tabchi_send_post(client=tbot, from_chat_id=chat_id, msg_id=msg_id, target_chat_id=chat_id, quote=quote)
        update.answer(text="پیام برای بازبینی ارسال شد.")

    if call_data.startswith("tabchi_broadcast_pop_"):
        tabchi_jid = call_data[len("tabchi_broadcast_pop_"):]
        new_broadcast_data.pop(tabchi_jid)
        update.answer(text="عملیات لغو شد.")
        update.message.delete()

    if call_data.startswith("tabchi_broadcast_start_"):
        tabchi_jid = call_data[len("tabchi_broadcast_start_"):]
        tabchi_broadcast_starter(update, tabchi_id=tabchi_jid)

    if call_data == "add_tabchi":
        adminstatus = istadmin(tbot_id=None, user_id=clicked_user.id)
        if adminstatus == 1:
            update.answer(text="شماره تبچی را با کد کشور و بدون + وارد کنید.", show_alert=True)
            update.message.reply_text(text="شماره تبچی را با کد کشور و بدون + وارد کنید.", quote=False)
            new_tabchi["adder"] = clicked_user.id
            new_tabchi["status"] = 1
        else:
            update.answer(text="شما به این بخش دسترسی ندارید.", show_alert=True)


def schedule_checker():
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as E:
            print(f"schedule error:\n{traceback.format_exc()}")
            continue


def get_and_update_time():
    with open(Timing_file) as tr:
        timee = int(tr.read())
    with open(Timing_file, "w") as tw:
        tw.write(str(timee + 1))
    return timee


def thread_bot_manager(tbot, timee):
    print(tbot.name)
    tbot: Client
    try:
        bot_info = get_bot_info(tbot_id=tbot.me.id)
    except:
        return
    print("t1")
    if not bot_info["status"]:
        return
    print("t2")
    posts = bot_info["posts"]
    if len(posts) == 0:
        return
    print("t3")
    post_settings = bot_info["posts_settings"]
    duration_between_posts, send_at_once = post_settings.values()
    last_post_sent = bot_info["last_post_sent"]
    print("t4")

    if (timee % duration_between_posts) == 0:
        print("t5")
        if send_at_once:
            print("t6")
            for post in posts:
                chat_id, msg_id, quote, dogps, dopvs = post.values()
                chats = []
                if dogps:
                    chats += bot_info["gps"]
                if dopvs:
                    chats += bot_info["pvs"]
                for chat in chats:
                    try:
                        tabchi_send_post(client=tbot, from_chat_id=chat_id, msg_id=msg_id, target_chat_id=chat, quote=quote)
                        time.sleep(8)
                    except Exception as E:
                        # try:
                            # tbot.send_message(chat_id="me", text="خطایی در ارسال پیام به گروه {} رخ داد\n\n```{}```".format(chat_id, str(E)))
                        # except:
                            # print(E)
                        pass

        else:
            print("t7")
            post_id = (last_post_sent + 1) % len(posts)
            post = posts[post_id]
            chat_id, msg_id, quote, dogps, dopvs = post.values()
            chats = []
            if dogps:
                chats += bot_info["gps"]
            if dopvs:
                chats += bot_info["pvs"]
            for chat in chats:
                try:
                    tabchi_send_post(client=tbot, from_chat_id=chat_id, msg_id=msg_id, target_chat_id=chat, quote=quote)
                    time.sleep(8)
                except Exception as E:
                    # try:
                        # tbot.send_message(chat_id="me", text="خطایی در ارسال پیام به گروه {} رخ داد\n\n```{}```".format(chat_id, str(E)))
                    # except:
                        # print(E)
                    pass
            bot_info["last_post_sent"] = post_id
            save_bot_info(tbot_json=bot_info)


def scheduled_posts_manager():
    timee = get_and_update_time()
    print(f"timee: {timee}")
    for tbot in BOTS.values():
        threading.Thread(target=thread_bot_manager, args=(tbot, timee)).start()


def schedule_stater():
    schedule.every().minute.at(":01").do(scheduled_posts_manager)
    threading.Thread(target=schedule_checker).start()


def get_updates(bot_client: Client):
    bot_client.add_handler(handler=MessageHandler(tabchi_handler))


def PyFile_Restart():
    python = sys.executable
    # try:
    #     os.system("clear")
    # except:
    #     pass
    os.execl(python, python, *sys.argv)



BOTS_LIST = list(BOTS.values())
for BOT in BOTS_LIST:
    BOT: Client
    get_updates(BOT)

if __name__ == "__main__":
    try:
        schedule_stater()
        compose(BOTS_LIST + [bot])
    except Exception as e:
        print("Error in startup:", e)
