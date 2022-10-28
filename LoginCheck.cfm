<!--- Make sure we have Login name and Password --->
<CFPARAM NAME="Form.UserLogin" TYPE="string">
<CFPARAM NAME="Form.UserPassword" TYPE="string">


<!--- Find record with this Username/Password --->
<!--- If no rows returned, password not valid --->
<cfoutput>
<cfset thisYear = year(now())>
<cfset thisMonth = month(now())>  
<cfset firstOfTheMonth = createDate(thisYear, thisMonth, 1)>
<cfset dow = dayofWeek(firstOfTheMonth)>
<cfset pad = dow - 1>
<cfset fecha = 0>
<cfset days = daysInMonth(now())>
<cfset counter = pad + 1>    
</cfoutput>    
<cfloop index="x" from="1" to="#days#">
    <cfif x is day(now())>
     <cfset fecha = "#thisMonth#" & "/" & "#x#" & "/" & "#thisYear#">
     <cfset counter = counter + 1>
    </cfif>
</cfloop>       
    
<CFSET GetUser.RecordCount=0>
<CFQUERY NAME="GetUser" datasource="wolffdb_dsn">
  SELECT  *          
  FROM  Usuarios
  WHERE user_name = '#Form.UserLogin#'
  <!---  And user_password = '#secret#'--->
   
</CFQUERY>
 
<!--- If the username and password is correct ---> 
<CFIF GetUser.RecordCount EQ 1>
    <cfset manCrush = '#Form.UserPassword#' />
    <cfset encryptionKey = '#GetUser.user_llave#'/>
    <cfset secret = encrypt(
           manCrush,
           encryptionKey,
           "AES",
           "hex"
           ) />    
           
           
     <cfif secret EQ GetUser.user_password>      
       <!--- Remember user's logged-in status, plus --->
       <!--- ContactID and First Name, in structure --->
       <CFSET SESSION.Auth = StructNew()>
       <CFSET SESSION.Auth.IsLoggedIn        = "Yes">
       <CFSET SESSION.Auth.user_key          = GetUser.user_key>
       <CFSET SESSION.Auth.user_name         = GetUser.user_name>
	     <CFSET SESSION.Auth.user_password     = GetUser.user_password>
       <CFSET SESSION.Auth.user_nombre       = GetUser.user_nombre>
       <CFSET SESSION.Auth.user_apellido     = GetUser.user_apellido>       
       <CFSET SESSION.Auth.email             = GetUser.user_email>  
       <CFSET SESSION.Auth.user_role         = GetUser.user_role>
       <CFSET SESSION.Auth.user_cia          = GetUser.user_fk_cia_key>
       <CFSET SESSION.Auth.hoy               = DateFormat(Now(),"mm/dd/yyyy")>    
       <CFSET SESSION.Auth.edad              = ''> 
       <CFSET SESSION.Auth.grupo             = ''>	
       <CFSET SESSION.Auth.estudio           = ''>   
       <CFSET SESSION.Auth.desde             = ''>   
       <CFSET SESSION.Auth.hasta             = ''>    
       <CFSET SESSION.Auth.titulo            = ''>  
       <CFSET SESSION.Auth.tituloDesc        = ''>     
       <CFSET SESSION.Auth.accion            = "INQ">
  
       <cfif '#TRIM(SESSION.Auth.user_cia)#' EQ 1>  
        <cflocation url="ListarUserLinks.cfm">
       <cfelseif '#TRIM(SESSION.Auth.user_cia)#' EQ 11>  
          <cflocation url="../LF/index.cfm">
        <cfelseif '#TRIM(SESSION.Auth.user_cia)#' EQ 7>  
          <cflocation url="../RE/index.cfm">         
       </cfif>
    
      </cfif>
</cfif>
     <CFSET SESSION.Auth = StructNew()>
     <CFSET SESSION.Auth.IsLoggedIn        = "No">
     <CFSET SESSION.Auth.user_key          = ''>
     <CFSET SESSION.Auth.user_name         = ''>
	   <CFSET SESSION.Auth.user_password     = ''>
     <CFSET SESSION.Auth.user_nombre       = ''>
     <CFSET SESSION.Auth.user_apellido     = ''>     
     <CFSET SESSION.Auth.email             = ''>   
     <CFSET SESSION.Auth.user_role         = ''>
     <CFSET SESSION.Auth.user_cia          = ''>
     <CFSET SESSION.Auth.hoy               = ''>   
     <CFSET SESSION.Auth.edad              = ''>      
	   <CFSET SESSION.Auth.grupo             = ''>
     <CFSET SESSION.Auth.estudio           = ''>   
     <CFSET SESSION.Auth.desde             = ''>   
     <CFSET SESSION.Auth.hasta             = ''>  
     <CFSET SESSION.Auth.titulo            = ''> 
     <CFSET SESSION.Auth.tituloDesc        = ''>      
     <CFSET SESSION.Auth.accion            = ''>
 
<cflocation url="login.cfm?action=2">

  


 