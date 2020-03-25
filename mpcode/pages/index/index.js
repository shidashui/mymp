var common = require('../../utils/common.js')
const app = getApp()
const title_dict = {'home':'话题', 'activity':'活动', 'my':'我的'}

Page({
  data: {
		title:'话题',
    PageCur: 'home', 
		modalName: app.globalData.modalName
  },
  NavChange(e) {
		let cur = e.currentTarget.dataset.cur
    this.setData({
      PageCur: cur,
			title: title_dict[cur]
    })
  },
  onShareAppMessage() {
    return {
      title: 'ColorUI-高颜值的小程序UI组件库',
      imageUrl: '/images/share.jpg',
      path: '/pages/index/index',
    }
  },
	/**
	 * 生命周期函数--监听页面加载
	 */
	onLoad: function (options) {
	},
	authUserInfo(e){
		wx.login({
		  success (res) {
		    // console.log('asdfasdf',res)
		  }
		}) 
		console.log('ok', e)
		var userInfo = e.detail.userInfo
		app.globalData.userInfo = userInfo
		common.userInfoSetInSQL(userInfo)
		
		this.setData({
			modalName: null
		})
	}
})