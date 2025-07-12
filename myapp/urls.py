
from django.contrib import admin

from django.urls import path

from myapp import views

urlpatterns = [


    path('Login_get/',views.Login_get),
    path('Login_post/',views.Login_post),
    path('Changepassword_get/',views.Changepassword_get),
    path('Changepassword_post/',views.Changepassword_post),
    path('companyview_get/',views.companyview_get),
    path('companyview_post/',views.companyview_post),
    path('approvecompany/<id>',views.approvecompany),
    path('rejectcompany/<id>',views.rejectcompany),
    path('guideview_get/',views.guideview_get),
    path('guideview_post/',views.guideview_post),
    path('approveguide/<id>',views.approveguide),
    path('rejectguide/<id>',views.rejectguide),
    path('viewApprovedCompany_get/',views.viewApprovedCompany_get),
    path('viewApprovedCompany_post/',views.viewApprovedCompany_post),
    path('viewApprovedGuide_get/',views.viewApprovedGuide_get),
    path('viewApprovedGuide_post/',views.viewApprovedGuide_post),
    path('viewRegisteredUsers_get/',views.viewRegisteredUsers_get),
    path('viewRegisteredUsers_post/',views.viewRegisteredUsers_post),
    path('motivationalVideo_get/',views.motivationalVideo_get),
    path('motivationalVideo_post/',views.motivationalVideo_post),
    path('adminlogout/',views.adminlogout),
    path('adminhome_get/',views.adminhome_get),
    # guide
    path('register_get/',views.register_get),
    path('register_post/',views.register_post),
    path('changepassword_get/',views.changepassword_get),
    path('changepassword_post/',views.changepassword_post),
    path('viewprofile_get/',views.viewprofile_get),
    path('edit_get/<id>',views.edit_get),
    path('edit_post/',views.edit_post),
    path('viewrequestfromuser_get/',views.viewrequestfromuser_get),
    path('viewapprovedrequest_get/',views.viewapprovedrequest_get),

    path('guidehome_get/',views.guidehome_get),
    path('guide_viewRegisteredUsers_get/',views.guide_viewRegisteredUsers_get),
    path('guide_viewRegisteredUsers_post/',views.guide_viewRegisteredUsers_post),

    path('acceptrequest_get/<id>', views.acceptrequest_get),
    path('rejectrequest_get/<id>', views.rejectrequest_get),

    #company

    path('c_register_get/', views.c_register_get),
    path('c_register_post/', views.c_register_post),
    path('c_changepassword_get/', views.c_changepassword_get),
    path('c_changepassword_post/', views.c_changepassword_post),
    path('c_viewprofile_get/', views.c_viewprofile_get),
    path('c_edit_get/',views.c_edit_get),
    path('c_edit_post/', views.c_edit_post),
    path('addvacancy_get/', views.addvacancy_get),
    path('addvacancy_post/', views.addvacancy_post),
    path('editvacancy_get/', views.editvacancy_get),
    path('editvacancy_post/', views.editvacancy_post),
    path('viewvacancy_get/', views.viewvacancy_get),
    path('viewvacancy_post/', views.viewvacancy_post),
    path('viewrequest_qualification_get/', views.viewrequest_qualification_get),
    path('viewrequest_qualification_post/', views.viewrequest_qualification_post),
    path('companyhome_get/', views.companyhome_get),
    path('c_acceptrequest_get/<id>', views.c_acceptrequest_get),
    path('c_rejectrequest_get/<id>', views.c_rejectrequest_get),


    #User

    path('userregister_get/', views.userregister_get),
    path('userregister_post/', views.userregister_post),
    path('u_changepassword_get/', views.u_changepassword_get),
    path('u_changepassword_post/', views.u_changepassword_post),
    path('u_viewprofile_get/', views.u_viewprofile_get),
    path('u_edit_get/', views.u_edit_get),
    path('u_edit_post/', views.u_edit_post),
    path('user_viewvacancy_get/', views.user_viewvacancy_get),
    path('user_viewvacancy_post/', views.user_viewvacancy_post),
    path('applyvacancy_get/<id>', views.applyvacancy_get),
    path('applyvacancy_post/', views.applyvacancy_post),
    # path('qualificationmngt_get/', views.qualificationmngt_get),
    # path('qualificationmngt_post/', views.qualificationmngt_post),
    path('viewstatus_get/', views.viewstatus_get),
    path('sendrequest_get/', views.sendrequest_get),
    path('sendrequest_post/<id>', views.sendrequest_post),
    path('u_viewApprovedCompany_get/', views.u_viewApprovedCompany_get),
    path('u_viewApprovedCompany_post/', views.u_viewApprovedCompany_post),
    path('u_viewApprovedGuide_get/', views.u_viewApprovedGuide_get),
    path('u_viewApprovedGuide_post/', views.u_viewApprovedGuide_post),
    path('userhome_get/', views.userhome_get),
    path('userhomeindex_get/', views.userhomeindex_get),



    path('chat1/<id>', views.chat1),
    path('chat_view/', views.chat_view),
    path('chat_send/<msg>', views.chat_send),

    path('chat2/<id>', views.chat2),
    path('chat_view2/', views.chat_view2),
    path('chat_send2/<msg>', views.chat_send2),

]
