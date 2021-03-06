var common = require('../../../utils/common.js')
const app = getApp();

Component({
  options: {
    addGlobalClass: true,
  },
  data: {
		StatusBar: app.globalData.StatusBar,
		CustomBar: app.globalData.CustomBar,
    TabCur: 0,
		tabNav:['全部','最新','热点'],
		scrollLeft:0
  },
	methods:{
		//跳转到发布页
		test(e){
			common.userLogin()
		},
		toAdd(e){
			wx.navigateTo({
				url:'../home/add/add',
			})
		},
		//跳到详情页
		toDetail(e){
			console.log('跳转')
			wx.navigateTo({
				url:'../home/detail/detail',
			})
		},
		tabSelect: function(e) {
			this.setData({
				TabCur: e.currentTarget.dataset.id,
				scrollLeft: (e.currentTarget.dataset.id-1)*60
			})
		}
	}
})
