//用户登陆
function userLogin(self) {
  wx.checkSession({
    success: function () {
      //存在登陆态
			console.log('self->',self)
			self.modalName = 'Modal'
    },
    fail: function () {
      //不存在登陆态
      onLogin()
			self.modalName = "Modal" 
			console.log('self->',self) 
    }
  })
} 

function onLogin() {
  wx.login({
    success: function (res) { 
      if (res.code) {
        //发起网络请求
        wx.request({
          url: 'http://127.0.0.1:8000/auth/',
          data: {
            code: res.code
          },
					header:{
						"content-type": "application/json"
					},
					method:"POST",
          success: function (res) {
            if (true) {  
              //获取到用户凭证 存儲 token 
              var json = res.data.data
              wx.setStorage({ 
                key: "token", 
                data: json.token
              })
              // getUserInfo()
            }
            else {

            }
          },
          fail: function (res) {

          }
        })
      }
    },
    fail: function (res) {
  
    }
  })

}

// function getUserInfo() {
// 	wx.getSetting({
// 		success(res){
// 			if (!res.authSetting['scope.userInfo']) {
// 				console.log('there')
// 				wx.authorize({
// 					scope:'scope.userInfo',
// 					success(){
// 						wx.getUserInfo({
// 							success: function (res) {
// 								var userInfo = res.userInfo
// 								userInfoSetInSQL(userInfo)
								
// 								// 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
// 								// 所以此处加入 callback 以防止这种情况
// 								if (this.userInfoReadyCallback) {
// 									this.userInfoReadyCallback(res)
// 								}
// 							},
// 							fail: function () {
// 								// userAccess() 
// 								console.log('fail')
// 							}
// 						}) 
// 					},
// 					fail(){
// 						console.log('没有授权')
// 					}
// 				})
// 			} else {
// 				console.log('test')
// 			}
// 		}
// 	})
// }

function userInfoSetInSQL(userInfo) {
	console.log('userInfo->', userInfo)
  wx.getStorage({
    key: 'token',
    success: function (res) {
      wx.request({
        url: 'http://127.0.0.1:8000/v1/user/',
        data: {
          third_Session: res.data,
          nickName: userInfo.nickName,
          avatarUrl: userInfo.avatarUrl,
          gender: userInfo.gender,
          province: userInfo.province,
          city: userInfo.city,
          country: userInfo.country
        },
        success: function (res) {
          if (res) {
            //SQL更新用户数据成功
          }
          else {
            //SQL更新用户数据失败
          }
        }
      })
    }
  })
}

module.exports = {
	onLogin:onLogin,
  userLogin:userLogin,
	userInfoSetInSQL:userInfoSetInSQL
} 