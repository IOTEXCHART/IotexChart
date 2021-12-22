from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),

	path("banner/", views.BannerView, name="banner"),

	path("unvetted/", views.unvetted, name="unvetted"),
	path('verify/banner/<int:pk>/', views.VerifyBannerView, name="verify_banner"),
	path('verify/vetted/<int:pk>/', views.VerifyVettedView, name="verify_vetted"),

	path("signup/", views.signup, name='signup'),
    path("signin/", views.signin, name='signin'),
	path('all-banner/', views.AllBannerView, name="all_banner"),

	path('all-vetted/', views.AllVettedView, name="all_vetted"),


	#coin urls 
	path("staking/", views.StakingView, name="staking"),
	path("your-stake/", views.YourStakeView, name="your_stake"),
	path("imagictoken/", views.ImagicTokenView, name="imagictoken"),
	path("metanyx/", views.MetanyxView, name="metanyx"),
	path("iotex-shiba/", views.IotexShibaView, name="iotex_shiba"),
	path("iotex/", views.IotexView, name="iotex"),
	path("zoom-swap/", views.ZoomSwapView, name="zoom_swap"),
	path("vitality/", views.VitalityView, name="vitality"),
	path("wow/", views.WowSwapView, name="wow"),
	path("game-fantasy-token/", views.GameFantasyTokenView, name="game_fantasy_token"),

]

