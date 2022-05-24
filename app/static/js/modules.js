
//*****************************************************************
//	MODULES
//*****************************************************************


	// TOP HEADER
	function loadTopHeader() {
		var s = '<section id="topbar" class="d-none d-lg-block">';
		s +=	'	<div class="container clearfix">';
		s +=	'		  <div class="contact-info float-start"> ';
		s +=	'				<i class="fa fa-envelope-o"></i> <a href="mailto:contact@allstatesmed.com">contact@allstatesmed.com</a>    ';   
		s +=	'		  </div> ';
		s +=	'		  <div class="social-links float-end"> ';
		//s +=	'				<!--<a href="#" class="twitter"><i class="fa fa-twitter"></i></a>  ';
		//s +=	'				<a href="#" class="facebook"><i class="fa fa-facebook"></i></a> ';
		//s +=	'				<a href="#" class="instagram"><i class="fa fa-instagram"></i></a> ';
		//s +=	'				<a href="#" class="google-plus"><i class="fa fa-google-plus"></i></a> ';
		//s +=	'				<a href="#" class="linkedin"><i class="fa fa-linkedin"></i></a> -->';
		s +=	'				<i class="fa fa-phone"></i> <a href="tel:+18005414879">+1 (800) 541-4879</a>';
		s +=	'		  </div>';
		s +=	'	</div> ';
		s +=	'</section>';
		
		$('#topheader').html(s); 

	}

	
	// HEADER
	function loadHeader() {
		var s = '<header id="header"> ';
		s += '		<div class="container"> ';
		s += '			<div id="logo" class="float-start"> ';
		s += '				<a href="#body" class="scrollto"><img src="../../assets/img/logo.png" alt="All States Medical Equipment and Distribution" width="65" /></a> ';
		s += '			</div> ';
		s += '			<nav id="nav-menu-container"> ';
		s += '				<ul class="nav-menu"> ';
		s += '					<li class="menu-active"><a href="#body">Home</a></li>	';
		s += '					<li><a href="#services">Services</a></li>		   ';
		s += '					<li><a href="#about">About Us</a></li>          ';
		s += '					<li><a href="#contact">Contact</a></li> ';
		s += '					<li><a href="https://allstatesmed.com"><kbd> &nbsp; SHOP &nbsp; </kbd></a></li> ';
		s += '				</ul> ';
		s += '			</nav> ';
		s += '		</div> ';
		s += '	</header> ';
		
		$('#header').html(s); 
		
	}
	
//*****************************************************************
//	MAIN
//*****************************************************************

	function Initialize() {
		loadTopHeader();
		loadHeader();
		
	}
	