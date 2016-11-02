$(document).ready(function() {
    blog.init();
    $('#search-blog-form').on('submit', function(e){
      e.preventDefault();
      blog.search_blog($('#search-feed').val())
    });
    $('#blog-form').on('submit', function(e){
      e.preventDefault();
      blog.create();
    });
    $('#edit-blog-form').on('submit', function(e){
      e.preventDefault();
      blog.update();
    });
    

});

var Blog = function() {
    this.init = function(){
      var self = this;
      $.ajax({  
          type: "GET",  
          url: ALL_BLOGS,
          dataType: "json",
          beforeSend: function(){$(".loader").show()},
          success: function(res) { 
              self.load_blogs(res, 6);
          }  
      }).done(function(){$(".loader").hide()});
    }
    this.load_blogs = function(data, number){
      var html = '';
      if(data.length!=0){
        if(data.length<number){number=data.length}
        for(var i = 0; i < number; i++) {
          html += '<div class="panel panel-danger col-md-8 col-sm-12 blog-panel">\
                  <div class="panel-heading teal">\
                      <a href="blog/'+data[i].slug+'/">\
                      <h3 class="panel-title white-text">'+ data[i].title +'</h3></a>\
                  </div>\
                  <div class="panel-body">\
                      <p>'+data[i].body+'</p>\
                  </div>\
                  <span style="padding:10px;">Created by <a href="'+data[i].creator.profile_url+'">@'+ data[i].creator.username +'</a></span>\
              </div>';          
        }
      } else {
        html = '<div class="alert alert-dismissible alert-info">\
                  <button type="button" class="close" data-dismiss="alert">×</button>\
                  <strong>OOPs!</strong> No records found.</div>'
      }
      $("#blog-div").html(html);
    }
    this.search_blog = function(term){
      var self = this;
      $("#blog-div").empty();
      $.ajax({  
          type: "GET",  
          url: SEARCH_BLOG,
          data: 'term='+term,
          dataType: "json",
          beforeSend: function(){$(".loader").show()},
          success: function(res) {
              self.load_blogs(res, 50)
          }  
      }).done(function(){$(".loader").hide()});
    }
    this.create = function(){
      var self = this;
      $("#id_slug").val(self.slugify($('#id_title').val()));
      for (instance in CKEDITOR.instances) {
          CKEDITOR.instances[instance].updateElement();
      }
      $.ajax({  
          type: "POST",
          url: $('#blog-form').attr('action'),
          data: $('#blog-form').serialize(),
          dataType: "json",
          beforeSend: function(){$(".loader").show()},
          success: function(res) {
            console.log(res.success)
            if(res.success){
              $.toaster({ priority : 'success', title : 'Success!', message : res.message});
            } else {
              $.toaster({ priority : 'danger', title : 'Error!', message : res.message});
            }
          },
          error: function(res){
            console.log(res.responseText)
            $.toaster({ priority : 'danger', title : 'Error!', message : 'Body can not be empty.'});
          }
      }).done(function(){$(".loader").hide()});      

    }
    this.update = function(){
      var self = this;
      $("#id_slug").val(self.slugify($('#id_title').val()));
      for (instance in CKEDITOR.instances) {
          CKEDITOR.instances[instance].updateElement();
      }
      $.ajax({  
          type: "PUT",
          url: $('#edit-blog-form').attr('action'),
          data: $('#edit-blog-form').serialize(),
          dataType: "json",
          headers: {"X-HTTP-Method-Override": "PUT", "X-CSRFToken": getCookie("csrftoken")},
          beforeSend: function(){$(".loader").show()},
          success: function(res) {
            console.log(res.success)
            if(res.success){
              $.toaster({ priority : 'success', title : 'Success!', message : res.message});
            } else {
              $.toaster({ priority : 'danger', title : 'Error!', message : res.message});
            }
          },
          error: function(res){
            console.log(res.responseText)
            $.toaster({ priority : 'danger', title : 'Error!', message : 'Body can not be empty.'});
          }
      }).done(function(){$(".loader").hide()});      

    }
    this.delete = function(id){
      var self = this;
      $.ajax({  
          type: "DELETE",
          url: $('#delete-blog').attr('href'),
          dataType: "json",
          headers: {"X-HTTP-Method-Override": "DELETE", "X-CSRFToken": getCookie("csrftoken")},
          beforeSend: function(){$(".loader").show()},
          success: function(res) {
            console.log(res)
            $.toaster({ priority : 'success', title : 'Success!', message : 'Blog Deleted.'});
            window.location = "/";
          },
      });      

    }
    this.slugify = function(Text)
    {
        return Text
            .toLowerCase()
            .replace(/ /g,'-')
            .replace(/[^\w-]+/g,'')
            ;
    }
}

var blog = new Blog();

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }
function delete_blog(id){
  blog.delete(id)
}
