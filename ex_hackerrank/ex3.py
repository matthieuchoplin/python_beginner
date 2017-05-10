thickness = 5
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust((thickness-1),' ')+c+(c*i).ljust((thickness-1), ' '))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness+2, ' ')+(c*thickness).rjust((thickness*4), ' '))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*thickness).rjust((thickness*thickness+2), ' '))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness+2, ' ')+(c*thickness).rjust((thickness*4), ' '))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust((thickness*thickness-1),' ')+c+(c*(thickness-i-1)).ljust((thickness*thickness-1),' ')))
