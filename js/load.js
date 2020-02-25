<script>
  window.addEventListener("load", function(event) {
    console.log("All resources finished loading!");
  });

  // or
  window.onload=function(){
    console.log("All resources finished loading!");
  };

  // HTML
  <body onload="SomeJavaScriptCode">

  // jQuery
  $( window ).on( "load", handler )
</script>
