current_session = {

    "resume":None,

    "jd":None

}


# src/core/session_store.py

active_resume = None


def set_active_resume(filename: str):

    global active_resume

    active_resume = filename


def get_active_resume():

    return active_resume


def set_jd(
        jd:str
):

    current_session[
        "jd"
    ]=jd


def get_jd():

    return current_session[
        "jd"
    ]