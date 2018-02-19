// script.name = SE_stripDocument.jsx;
// script.description = Batch opening and removing of particular elements, then saves as EPS;
// script.requirements = none
// script.parent = Benjamin Hamilton
// script.elegant = false;



var folder = Folder.selectDialog("Select Source Folder..."); // select folder
var nameArray = [];

if (folder==null) {
                    alert("Good Bye");
}


else {
    var files = find_files (folder, ['.svg']);
          var fileCount = files.length; // count them


          if (fileCount>0) {
                    for (i=0; i<fileCount; i++) {
                        var currentDoc = app.open(files[i]);
                        // stripDocument();
                        expandAllItems();
                        saveAsEPS();
                        currentDoc.close();

                    }
        alert(fileCount + ' file(s) processed');
          }
          else {
                    alert("There are no files in this folder.");
          }
}


// recurse subfolders - Peter Kharel
function find_files (dir, mask_array){
    var arr = [];
    for (var i = 0; i < mask_array.length; i++){
        arr = arr.concat (find_files_sub (dir, [], mask_array[i].toUpperCase()));
    }
    return arr;
}

function find_files_sub (dir, array, mask){
    var f = Folder (dir).getFiles ( '*.*' );
    for (var i = 0; i < f.length; i++){
        if (f[i] instanceof Folder){
            find_files_sub (f[i], array, mask);
        } else if (f[i].name.substr (-mask.length).toUpperCase() == mask){
            array.push (f[i]);
        }
    }
    return array;
}

function expandAllItems(){
    app.doScript('expandAllItems','Default Actions');
 }



function saveAsEPS() {
    var newFile = new File(folder);
    var epsOptions = new EPSSaveOptions();
    currentDoc.saveAs( newFile, epsOptions);
}
