showroom = set()

showroom.update(('Accent', 'Wrangler', 'Sonata', 'Fusion'))

print(showroom)
print("The length of my set is "+str(len(showroom)))

showroom.add('Accent')

showroom.update(('F-150', 'Excursion'))

showroom.discard('F-150')
print(showroom)


junkyard = set()
junkyard.update(('F-150','Camero','Wrangler','Sonata'))

print("Cars in both show room and junkyard: "+ str(showroom&junkyard))
showroom = showroom|junkyard
print('My new showroom with both sets = '+str(showroom))

showroom.discard('Wrangler')
showroom.discard('F-150')
print('My final showroom: '+ str(showroom))
