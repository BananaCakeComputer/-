'''
作者：蕉饼电脑
2021.1.17
需安装cdmaoapi以及easygui
'''
import cdmaoapi
import easygui
def fillpost(postid):
    print('loading...')
    ans = easygui.ynbox(cdmaoapi.CdmaoForumIn(postid).postTitle + '\n\n点击量:' + str(cdmaoapi.CdmaoForumIn(postid).postView) + '\n\n————————————————————————————————————\n\n' + cdmaoapi.CdmaoForumIn(postid).writerName + ' ((' + str(cdmaoapi.CdmaoForumIn(postid).writerStudLevel) + ')' + cdmaoapi.CdmaoForumIn(postid).writerStudName + ')\n\n' + cdmaoapi.CdmaoForumIn(postid).content,'编程猫社区- ' + cdmaoapi.CdmaoForumIn(postid).postTitle + ' -编程学习交流',('评论','关闭'))
    if ans:
        ans = str(easygui.enterbox('评论','编程猫社区- ' + cdmaoapi.CdmaoForumIn(postid).postTitle + ' -编程学习交流'))
        cdmaoapi.CdmaoForumIn(postid).SubmitComment(ans)
ans = easygui.ynbox('选择','编程猫论坛',('搜索帖子','其他功能'))
if ans:
    ans = str(easygui.enterbox('标题关键字？','编程猫论坛','搜索帖子'))
    allPost = cdmaoapi.CdmaoSeaForum(ans)
    ans = easygui.ynbox('为您找到"' + ans + '"相关的帖子，共' + str(len(allPost['postId'])) + '篇帖子','编程猫论坛',('查看','关闭'))
    if ans:
        postid = allPost['postId']
        posttitle = allPost['postTitle']
        writername = allPost['writerName']
        studioname = allPost['writerStudName']
        studiolevel = allPost['writerStudLevel']
        i = 0
        while i < len(postid):
            ans = easygui.ynbox(writername[i] + ' ((' + str(studiolevel[i]) + ')' + studioname[i] + ')\n\n' + posttitle[i],'编程猫论坛',('打开','下一个'))
            if ans:
                fillpost(postid[i])
                break
            i += 1
else:
    ans = easygui.ynbox('选择','编程猫论坛',('按帖ID搜索','发布帖子'))
    if ans:
        ans = easygui.enterbox('帖ID','编程猫论坛','356802')
        fillpost(ans)
    else:
        title = easygui.enterbox('输入标题','发帖','【发帖关键字】请输入标题（5-50字符以内）')
        if len(title)<5 or len(title)>50:
            easygui.msgbox('请填写5-50字的标题','发帖')
        else:
            content = easygui.enterbox('输入内容','发帖','论坛内容（至少10字）支持HTML')
            if len(content)<10:
                easygui.msgbox('帖子内容至少10个字','发帖')
            else:
                cdmaoapi.CdmaoForumSubmit(title,content,1)
