from django.shortcuts import render
from .models import (
    HeaderText,
    FooterText,
    TreeBlocks,
    LeftBlock,
    RightBlock,
    WorkProcess,
    Reviews,
    PricingPlan,
    Counter,
    Blog
)


def index(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "tree_blocks": TreeBlocks.objects.all(),
        "left_block": LeftBlock.objects.all().first(),
        "right_block": RightBlock.objects.all().first(),
        "work_process_items": WorkProcess.objects.all(),
        "reviews": Reviews.objects.all(),
        "pricing_plan": PricingPlan.objects.all(),
        "counter": Counter.objects.all().first(),
        "all_blogs": Blog.objects.all()
    }
    return render(request, "home.html", context)


def single_blog(request, blog_id):
    # id = Blog.objects.all()[blog_id].id - 1
    blog = Blog.objects.get(id=blog_id)

    print(blog)

    print(id)
    return render(request, "single_blog.html", {
        "blog": blog
    })
