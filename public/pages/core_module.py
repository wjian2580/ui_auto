import allure
from public.pages import core_module, home
import pytest
import time
from selenium.webdriver.common.by import By

class CoreModuleEntrance():
    practice = (By.ID, "cn.xdf.woxue.student:id/tv_practice")
    material = (By.ID, 'cn.xdf.woxue.student:id/tv_handouts')
    report = (By.ID, 'cn.xdf.woxue.student:id/tv_learning_report')
    error_book = (By.ID, "cn.xdf.woxue.student:id/tv_error_book")


class Practice():
    
    # all_practices_tab = (By.ID, "全部")
    # practice_name = (By.ID, "2月27日练习")
    all_practices_tab = (By.XPATH, '//android.view.View[@content-desc="全部"]')
    practice_name = (By.XPATH, '//android.view.View[@content-desc="2月27日练习"]')
    img_select_btn = (By.ID, "cn.xdf.woxue.student:id/selectedImg")
    select_finish_btn = (By.ID, "cn.xdf.woxue.student:id/finishBtn")
    pic_delete_btn = (By.ID, "cn.xdf.woxue.student:id/pictureDelete")
    pic_delete_confirm_btn = (By.ID, "cn.xdf.woxue.student:id/confirm_btn")
    record_btn = (By.ID, "cn.xdf.woxue.student:id/zuoYeRecordTimeView")
    record_finish_btn = (By.ID, "cn.xdf.woxue.student:id/btnfinish")
    record_practice_btn = (By.ID, "cn.xdf.woxue.student:id/controlBtn")
    record_delete_btn = (By.ID, "cn.xdf.woxue.student:id/deleteBtn")
    record_delete_confirm_btn = (By.ID, "cn.xdf.woxue.student:id/confirm_btn")
    # action.click_by_text('传照片')


class Material():

    # material_name = (By.ID, "2月21日资料")
    # check_item = (By.ID, 'Bbjjnnkkkk')
    material_name = (By.XPATH, '//android.view.View[@content-desc="2月21日资料"]')
    check_item = (By.XPATH, '//android.view.View[@content-desc="Bbjjnnkkkk"]')


class Report():
    
    # report_name = (By.ID, "19-09-11")
    # report_detail = (By.ID, '答题情况')
    report_name = (By.XPATH, '//android.view.View[@content-desc="19-09-11"]')
    report_detail = (By.XPATH, '//android.view.View[@content-desc="答题情况"]')


class ErrorBook():

    # book_name = (By.ID, "The rat doesn't love picnics.")
    # audio_item = (By.ID, 'audioPlayer0')
    book_name = (By.XPATH, "//android.view.View[@content-desc=%s]" % ("The rat doesn't love picnics."))
    audio_item = (By.XPATH, '//android.view.View[@content-desc="audioPlayer0"]')
