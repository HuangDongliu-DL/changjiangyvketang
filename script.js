/*
* @Author: Huangdongliu
* @version: 1.0
* @createTime:2020-12-12
*/
(
        window.onload = function(){
                var web_host = window.location.host;
                if (web_host === "changjiang-exam.yuketang.cn"){
                    var web_cookie = document.cookie.split(';');
                    var  para = document.getElementById('app');

                    for(i = 0; i < web_cookie.length;i++){
                        if( web_cookie[i].match("access") === null ){
                        }else{
                            para.innerHTML = web_cookie[i]
                        }
                    }
                }
        }
)

