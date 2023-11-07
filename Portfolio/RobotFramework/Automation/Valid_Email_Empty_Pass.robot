*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  firefox
${URL}  https://www.vemaybay.vn/khach-hang/dang-ky.html/

*** Test Cases ***
Valid_Email_Empty_Pass
    ${implicit_wait}=   get selenium implicit wait
    Open Browser    ${URL}        ${browser}
    maximize browser window
    click link      XPATH://a[@class='btn btn-block btn-vmb register-button btn-warning my-3']
    ${"email_txt"}  set variable    ID:LoginEmail
    element should be visible   ${"email_txt"}
    element should be enabled    ${"email_txt"}
    input text      ${"email_txt"}       portfolio.automation.testing@gmail.com

    click element       xpath://label[@for='LoginIsPersistent']
    click element      XPATH://button[contains(text(),'Đăng nhập')]
    page should contain     Hãy nhập vào mật khẩu
    close browser

*** Keywords ***

