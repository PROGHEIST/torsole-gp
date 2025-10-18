# TODO: Fix Navbar Dropdown Staying Open on Redirect

- [x] Import Router from @angular/router in navbar.ts
- [x] Inject Router in constructor of navbar.ts
- [x] In ngOnInit of navbar.ts, subscribe to router.events and on NavigationEnd, set isMenuOpen, isAboutOpen, isCitizenOpen, isRTIOpen to false
