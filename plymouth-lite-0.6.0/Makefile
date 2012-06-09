
ply-image: ply-image.c ply-frame-buffer.c Makefile
	gcc -O2 -march=core2 -mtune=generic -lm `pkg-config --cflags libpng12` `pkg-config --libs libpng12` ply-image.c ply-frame-buffer.c -o ply-image
	
clean:
	rm -f ply-image *~ gmon.out
	
install: ply-image
	mkdir -p $(DESTDIR)/usr/bin	
	mkdir -p $(DESTDIR)/usr/share/plymouth
	cp ply-image $(DESTDIR)/usr/bin
	cp splash.png $(DESTDIR)/usr/share/plymouth/splash.png
	
	