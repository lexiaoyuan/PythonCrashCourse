name_lists = ['dad', 'mom', 'yege', 'ruanwei']
print("Invite " + name_lists[0].title() + " to dinner!")
print("Invite " + name_lists[1].title() + " to dinner!")
print("Invite " + name_lists[2].title() + " to dinner!")
print("Invite " + name_lists[3].title() + " to dinner!")

print(name_lists[3].title() + " can't come fot dinner!")
name_lists.remove('ruanwei')
name_lists.append('yangxi')
print("Invite " + name_lists[0].title() + " to dinner!")
print("Invite " + name_lists[1].title() + " to dinner!")
print("Invite " + name_lists[2].title() + " to dinner!")
print("Invite " + name_lists[3].title() + " to dinner!")

print("I found a bigger table")
name_lists.insert(0, 'zhangliangyin')
name_lists.insert(3, 'shuchang')
name_lists.append('zhugedali')
print("Invite " + name_lists[0].title() + " to dinner!")
print("Invite " + name_lists[1].title() + " to dinner!")
print("Invite " + name_lists[2].title() + " to dinner!")
print("Invite " + name_lists[3].title() + " to dinner!")
print("Invite " + name_lists[4].title() + " to dinner!")
print("Invite " + name_lists[5].title() + " to dinner!")
print("Invite " + name_lists[6].title() + " to dinner!")

print("I can only invite two guests")
print("I'm sorry I can't invite " + name_lists.pop().title())
print("I'm sorry I can't invite " + name_lists.pop().title())
print("I'm sorry I can't invite " + name_lists.pop().title())
print("I'm sorry I can't invite " + name_lists.pop().title())
print("I'm sorry I can't invite " + name_lists.pop().title())

print("Invite " + name_lists[0].title() + " to dinner!")
print("Invite " + name_lists[1].title() + " to dinner!")

del name_lists[0]
del name_lists[0]
print(name_lists)
