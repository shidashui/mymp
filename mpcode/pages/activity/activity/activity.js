const app = getApp();

Component({
  options: {
    addGlobalClass: true,
  },
  data: {
		StatusBar: app.globalData.StatusBar,
		CustomBar: app.globalData.CustomBar,
  },
	methods:{
		isCard: function(e) {
		    console.log(e.detail.value)
		    this.setData({
		      isCard: e.detail.value
		    })
		  },
	}
})
