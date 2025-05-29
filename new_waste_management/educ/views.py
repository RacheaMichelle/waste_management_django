from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import QuizQuestion

def waste_quiz(request):
    questions = QuizQuestion.objects.all()
    paginator = Paginator(questions, 5)  # 5 questions per page
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        # Save user answers for current page in session
        user_answers = request.session.get('user_answers', {})

        for question in page_obj.object_list:
            answer = request.POST.get(str(question.id))
            if answer:
                user_answers[str(question.id)] = answer

        request.session['user_answers'] = user_answers

        # If not last page, redirect to next page
        if page_number < paginator.num_pages:
            next_page = page_number + 1
            return redirect(f"{request.path}?page={next_page}")
        else:
            # Last page: calculate score and prepare feedback
            score = 0
            total = questions.count()
            feedback = []

            for question in questions:
                user_answer = user_answers.get(str(question.id), None)
                is_correct = (
                    user_answer is not None and
                    user_answer.strip().lower() == question.correct_answer.strip().lower()
                )
                if is_correct:
                    score += 1
                feedback.append({
                    "question": question.question,
                    "correct_answer": question.correct_answer,
                    "user_answer": user_answer,
                    "explanation": question.explanation,
                    "is_correct": is_correct
                })

            # Clear stored answers after finishing
            if 'user_answers' in request.session:
                del request.session['user_answers']

            return render(request, "educ/quiz_result.html", {
                "score": score,
                "total": total,
                "feedback": feedback
            })

    return render(request, "educ/quiz.html", {
        "page_obj": page_obj,
        "paginator": paginator,
        "current_page": page_number,
    })
