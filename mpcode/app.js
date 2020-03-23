//app.js
App({
  onLaunch: function() {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录  
		wx.checkSession({
			success: function(){
				//存在登陆态
				console.log('success')
			},
			fail: function(){
				//不存在登陆态
				wx.login({
				  success: function (res) {
						console.log(res) 
				    if (res.code) {
				      //发起网络请求
				      wx.request({
				        url: 'http://127.0.0.1:8000/auth',
				        data: {
				          code: res.code
				        },
				        success: function (res) {
				          const self = this
									//获取到用户凭证 存儲 3rd_session 
									var json = JSON.parse(res.data.Data)
									wx.setStorage({
										key: "third_Session", 
										data: json.third_Session
									})
									// getUserInfo()
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
		})
    
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
    // 获取系统状态栏信息
    wx.getSystemInfo({
      success: e => {
        this.globalData.StatusBar = e.statusBarHeight;
        let capsule = wx.getMenuButtonBoundingClientRect();
        if (capsule) {
         	this.globalData.Custom = capsule;
        	this.globalData.CustomBar = capsule.bottom + capsule.top - e.statusBarHeight;
        } else {
        	this.globalData.CustomBar = e.statusBarHeight + 50;
        }
      }
    })
  },
  globalData: {
    userInfo: null
  }
})