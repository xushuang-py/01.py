const recipeStore = require('../../utils/recipe-store')

const defaultImage = 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=1200&q=90'

Page({
  data: {
    isEditing: false,
    saving: false,
    categories: ['快手菜', '下饭菜', '肉菜', '海鲜', '素食', '汤羹'],
    levels: ['简单', '进阶'],
    categoryIndex: 0,
    levelIndex: 0,
    form: {
      id: '', name: '', shortDesc: '', image: '', time: 20,
      category: '快手菜', level: '简单',
      ingredients: [{ name: '', amount: '' }],
      steps: ['']
    }
  },
  onLoad(options) {
    if (!options.id) return
    const recipe = recipeStore.getRecipe(options.id)
    if (!recipe) return
    const ingredients = recipe.ingredients.map(item => ({ name: item[0], amount: item[1] }))
    const categoryIndex = Math.max(0, this.data.categories.indexOf(recipe.category))
    const levelIndex = Math.max(0, this.data.levels.indexOf(recipe.level))
    this.setData({
      isEditing: true,
      categoryIndex,
      levelIndex,
      form: { ...recipe, ingredients }
    })
    wx.setNavigationBarTitle({ title: '修改菜谱' })
  },
  changeField(e) {
    this.setData({ [`form.${e.currentTarget.dataset.field}`]: e.detail.value })
  },
  changeCategory(e) {
    const categoryIndex = Number(e.detail.value)
    this.setData({ categoryIndex, 'form.category': this.data.categories[categoryIndex] })
  },
  changeLevel(e) {
    const levelIndex = Number(e.detail.value)
    this.setData({ levelIndex, 'form.level': this.data.levels[levelIndex] })
  },
  chooseImage() {
    wx.chooseMedia({
      count: 1,
      mediaType: ['image'],
      sourceType: ['album', 'camera'],
      success: result => {
        const tempFilePath = result.tempFiles[0].tempFilePath
        wx.saveFile({
          tempFilePath,
          success: saved => this.setData({ 'form.image': saved.savedFilePath }),
          fail: () => this.setData({ 'form.image': tempFilePath })
        })
      }
    })
  },
  addIngredient() {
    this.setData({ 'form.ingredients': [...this.data.form.ingredients, { name: '', amount: '' }] })
  },
  changeIngredientName(e) {
    this.setData({ [`form.ingredients[${e.currentTarget.dataset.index}].name`]: e.detail.value })
  },
  changeIngredientAmount(e) {
    this.setData({ [`form.ingredients[${e.currentTarget.dataset.index}].amount`]: e.detail.value })
  },
  removeIngredient(e) {
    if (this.data.form.ingredients.length === 1) return
    const ingredients = this.data.form.ingredients.filter((_, index) => index !== Number(e.currentTarget.dataset.index))
    this.setData({ 'form.ingredients': ingredients })
  },
  addStep() {
    this.setData({ 'form.steps': [...this.data.form.steps, ''] })
  },
  changeStep(e) {
    this.setData({ [`form.steps[${e.currentTarget.dataset.index}]`]: e.detail.value })
  },
  removeStep(e) {
    if (this.data.form.steps.length === 1) return
    const steps = this.data.form.steps.filter((_, index) => index !== Number(e.currentTarget.dataset.index))
    this.setData({ 'form.steps': steps })
  },
  saveRecipe() {
    const form = this.data.form
    if (!form.name.trim()) {
      wx.showToast({ title: '请填写菜名', icon: 'none' })
      return
    }
    const ingredients = form.ingredients.filter(item => item.name.trim()).map(item => [item.name.trim(), item.amount.trim() || '适量'])
    const steps = form.steps.map(item => item.trim()).filter(Boolean)
    if (!ingredients.length || !steps.length) {
      wx.showToast({ title: '请填写食材和制作步骤', icon: 'none' })
      return
    }
    this.setData({ saving: true })
    recipeStore.saveRecipe({
      ...form,
      id: form.id || `custom-${Date.now()}`,
      name: form.name.trim(),
      shortDesc: form.shortDesc.trim() || '我的家常菜 · 用心做好味',
      image: form.image || defaultImage,
      time: Number(form.time) || 20,
      ingredients,
      steps
    })
    wx.showToast({ title: '保存成功', icon: 'success' })
    setTimeout(() => wx.navigateBack(), 500)
  }
})
