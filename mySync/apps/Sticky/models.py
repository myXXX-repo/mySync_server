from mySync.common.ext import db


class Sticky(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(1024))
    con = db.Column(db.String(1024))
    dev_name = db.Column(db.String(1024))
    create_time = db.Column(db.String(1024))
    update_time = db.Column(db.String(1024))
    ip = db.Column(db.String(1024))

    # 对于客户端app包含
    # 创建时间戳 该条记录创建的时间戳
    # 更新本地时间戳 本地进行编辑的时间戳
    # 更新远程时间戳 对于本地将本条数据成功上传到服务器的时刻更新
    # 内容 是一个json数组字符串 [{time:...,con:...},{...},{...},{}] 数组中元素用于保存不同版本的数据
    #     内容可以进行回溯 时间用于标定第几个版本 顺序号 在服务端和客户端均以此方式保存

    # 服务端 仅保存 创建时间戳和上次更新时间戳

    # 保证客户端服务器上记录的相应时间戳一致的方法
    # 客户端上传数据，获得服务器返回数据后，再保存新的数据（时间戳 或其他），一旦出现问题 直接抛弃时间戳的更改

    # 客户端通过比较本地的 更新远程时间戳 和 服务器的 上次更新时间戳
    #       并且服务器的 上次更新时间戳 和本地的 更新远程时间戳 一致 则直接上传更新
    #       并且服务器的 上次更新时间戳 和本地的 更新远程时间戳 相比 小 则代表服务器端或客户端时间保存出现问题 需要特别处理
    #       并且服务器的 上次更新时间戳 和本地的 更新远程时间戳 相比 大

    # 客户端上传数据 根据创建时间戳唯一确认一条记录


# def add_one(title, con, time, dev_name, ip):
#     sticky = Sticky()
#     sticky.title = title
#     sticky.con = con
#     sticky.create_time = time
#     sticky.dev_name = dev_name
#     sticky.ip = ip
#
#     db.session.add(sticky)
#     db.session.commit()


def add_ones(stickies=None):
    if stickies is None:
        stickies = []
    for i in stickies:
        db.session.add(i)
    db.session.commit()


def getAll():
    sticky = Sticky()
    result = sticky.query.all()
    return result


def del_all():
    result = -1
    try:
        db.session.query(Sticky).delete()
        result = 0
    except:
        db.session.rollback()
    finally:
        db.session.commit()
    return result
