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
    Counter
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
    }
    return render(request, "base.html", context)
