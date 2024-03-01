import os

if not os.path.exists("./posts"):
    os.mkdir("./posts")
    print("posts are stored in format dd-mm-yyyy-title.html")
    print("posts support spaces in the title and html formatting")
    print("no posts exist, exiting")
    exit()
if not os.path.exists("./export/posts"):
    os.makedirs("./export/posts")

def generate_index(title, posts, email):
    index = f"""
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap"
      rel="stylesheet"
    />
    <title>{title}</title>
  </head>
  <body>
    <header>
      <h1>{title}</h1>
    </header>

    {posts}
    
    <footer>
      <div class="email">
        email: <a href="mailto:{email}">{email}</a>
      </div>
      <div class="watermark">
        made with ❤️ by
        <a href="https://github.com/uthmn" target="_blank">@uthmn</a>
      </div>
    </footer>
  </body>
  <style>
    * {{
      font-family: "Manrope", sans-serif;
      font-optical-sizing: auto;
      min-width: 0;
      color: #1b1b1b;
    }}

    /*
    .manrope-<uniquifier> {{
      font-family: "Manrope", sans-serif;
      font-optical-sizing: auto;
      font-weight: <weight>;
      font-style: normal;
    }}
    */


    body {{
      background-color: #F8F8FF;
    }}

    header {{
      position: -webkit-sticky; /* Safari */
      position: sticky;
      top: 0;
      background-color: #F8F8FF;
    }}

    .blog-sec {{
      overflow-wrap: break-word;
      max-width: 32em;
    }}

    footer {{
      position: -webkit-fixed; /* Safari */
      position: fixed;
      bottom: 0;
      content: "";
      left: 0;
      width: 100%;
      white-space: nowrap;
      display: inline-block;
      background-color: #F8F8FF;
    }}

    .watermark {{
      color: rgba(50,50,50,0.75);
      display: inline-block;
      float: right;
    }}

    .watermark a {{
      color: #8a2be2;
    }}

    .email {{
      display: inline-block;
      text-decoration: none;
    }}

    .email a {{
      color: #8a2be2;
    }}

    a {{
      text-decoration: none; !important
    }}
  </style>
</html>
    """
    
    with open("./export/index.html", "w", encoding="utf-8") as file:
        file.write(index)
    
def generate_posts_sec():
    # posts are stored in format dd/mm/yyyy/title
    
    posts = []
    post_titles = os.listdir("./posts")
    
    for i in range(len(post_titles)):
        href = f"export/posts/{post_titles[i]}.html"
        title = post_titles[i][11:]
        old_date = post_titles[i][:10]
        date = old_date.replace("-", "/")
        description = ""
        
        with open(f"posts/{post_titles[i]}", "r") as file:
            description = file.read()[:256] + "..."
        
        post = f"""
        <div class="blog-sec">
            <a href="{href}">
                <h2>{title}</h2>
                <p>{date}</p>
                <p>
                    {description}
                </p>
            </a>
        </div>
        """
        
        posts.append(post)
    
    return posts

def generate_post_pages():
    post_titles = os.listdir("./posts")
    
    for i in range(len(post_titles)):
        title = post_titles[i]
        export = f"export/posts/{title}.html"
        content = ""
        
        with open(f"./posts/{title}", "r") as file:
            content = file.read()
        
        index = f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <link rel="preconnect" href="https://fonts.googleapis.com" />
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
                <link
                    href="https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap"
                    rel="stylesheet"
                />
                <title>{title}</title>
            </head>
            <body>
                {content}
            </body>
            <style>
                * {{
                    font-family: "Manrope", sans-serif;
                }}
            </style>
        </html>
        """
        
        with open(export, "w") as file:
            file.write(index)

generate_post_pages()
generate_index("Uthmn - blog", str(''.join(generate_posts_sec())), "admin@uthmn.com")