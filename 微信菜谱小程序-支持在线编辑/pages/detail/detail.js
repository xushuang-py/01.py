const recipeStore = require('../../utils/recipe-store')

Page({
  data: { recipe: null, recipeId: '' },
  onLoad(options) {
    this.setData({ recipeId: options.id || '' })
    this.loadRecipe()
  },
  onShow() {
    if (this.data.recipeId) this.loadRecipe()
  },
  loadRecipe() {
    const recipes = recipeStore.getRecipes()
    const recipe = recipeStore.getRecipe(this.data.recipeId) || recipes[0]
    const saved = wx.getStorageSync('recipeFavorites') || {}
    this.setData({ recipe: { ...recipe, favorite: !!saved[recipe.id] } })
  },
  goBack() { wx.navigateBack() },
  editRecipe() {
    wx.navigateTo({ url: `/pages/editor/editor?id=${this.data.recipe.id}` })
  },
  toggleFavorite() {
    const recipe = { ...this.data.recipe, favorite: !this.data.recipe.favorite }
    const saved = wx.getStorageSync('recipeFavorites') || {}
    recipe.favorite ? saved[recipe.id] = true : delete saved[recipe.id]
    wx.setStorageSync('recipeFavorites', saved)
    this.setData({ recipe })
  }
})
