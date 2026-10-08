const recipeStore = require('../../utils/recipe-store')

Page({
  data: { recipes: [] },
  onShow() {
    this.setData({ recipes: recipeStore.getRecipes() })
  },
  addRecipe() {
    wx.navigateTo({ url: '/pages/editor/editor' })
  },
  editRecipe(e) {
    wx.navigateTo({ url: `/pages/editor/editor?id=${e.currentTarget.dataset.id}` })
  }
})
