<?php
    require "header.php";
?>

<div class="page">
  <div class="container15">
    <div class="camerabox">
      <div class="form10">
        <div class="Neon Neon-theme-dragdropbox">
          <input style="z-index: 999; opacity: 0; width: 320px; height: 200px; position: absolute; right: 0px; left: 0px; margin-right: auto; margin-left: auto;" name="files[]" id="filer_input1" multiple="multiple" type="file" onchange="previewFile()">
          <div class="Neon-input-dragDrop"><div class="Neon-input-inner"><div class="Neon-input-icon"><i class="fa fa-file-image-o"></i></div><div class="Neon-input-text"><h3>Drag&amp;Drop files here</h3> <span style="display:inline-block; margin: 15px 0">or</span></div><a class="Neon-input-choose-btn blue">Browse Files</a></div></div>
        </div>
        <video class="view" autoplay="true" id="video" width="100%" height="100%"></video>
        <canvas class="canvas" id="canvas"></canvas>
        <img style="width: 100%; height: 100%; text-align: center" id="photo" src="" value="#" name="theImg">

        <input type="submit" id="captureSubmit" value="Take a Photo" name="captureSubmit">
        <input type="submit" id="filterAddSubmit0" value="Add a Star Sticker" name="filterAddSubmit0">
        <input type="submit" id="filterAddSubmit1" value="Add a Heart Sticker" name="filterAddSubmit1">
        <input type="submit" id="uploadSubmit" value="Upload" name="uploadSubmit">
        <img style="display: none" id="supImage0" src="">
        <img style="display: none" id="supImage1" src="">
      </div>
      <script type="text/javascript">
        function previewFile()
        {
          var preview = document.querySelector('img');
          var file    = document.querySelector('input[type=file]').files[0];
          var reader  = new FileReader();

          reader.onloadend = function () {
            preview.src = reader.result;
          }

          if (file) {
            reader.readAsDataURL(file);
          } else {
            preview.src = "";
          }
        }
        previewFile();

      </script>
      <script src="./JsCode/photo.js"></script>

      <br>
    </div>
  </div>
</div>

<?php
    require "footer.php";
?>