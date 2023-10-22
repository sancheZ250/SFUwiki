from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from wiki.models import Teacher, Review


@receiver(pre_save, sender=Teacher)
def check_department_institute(sender, instance, **kwargs):
    if instance.department.institute != instance.institute:
        raise ValidationError("Teacher's department must belong to the same institute.")


@receiver(post_save, sender=Review)
def update_teacher_ratings(sender, instance, created, **kwargs):
    if created:
        teacher = instance.teacher

        knowledge_rating = teacher.knowledge_rating
        teaching_skill_rating = teacher.teaching_skill_rating
        easiness_rating = teacher.easiness_rating
        communication_rating = teacher.communication_rating

        review_knowledge_rating = instance.knowledge_rating
        review_teaching_skill_rating = instance.teaching_skill_rating
        review_easiness_rating = instance.easiness_rating
        review_communication_rating = instance.communication_rating

        total_ratings = teacher.review_count
        new_teacher_knowledge_rating = (knowledge_rating * total_ratings + review_knowledge_rating) / (
                total_ratings + 1)
        new_teacher_teaching_skill_rating = (teaching_skill_rating * total_ratings + review_teaching_skill_rating) / \
                                            (total_ratings + 1)
        new_teacher_easiness_rating = (easiness_rating * total_ratings + review_easiness_rating) / (total_ratings + 1)
        new_teacher_communication_rating = (communication_rating * total_ratings + review_communication_rating) / (
                total_ratings + 1)
        new_teacher_avg_rating = (new_teacher_communication_rating + new_teacher_easiness_rating +
                                  new_teacher_teaching_skill_rating + new_teacher_knowledge_rating) / 4
        teacher.easiness_rating = new_teacher_easiness_rating
        teacher.teaching_skill_rating = new_teacher_teaching_skill_rating
        teacher.communication_rating = new_teacher_communication_rating
        teacher.knowledge_rating = new_teacher_knowledge_rating
        teacher.avg_rating = new_teacher_avg_rating
        teacher.review_count += 1
        teacher.save()


@receiver(pre_delete, sender=Review)
def update_teacher_ratings_on_review_delete(sender, instance, **kwargs):
    teacher = instance.teacher
    if teacher.review_count > 1:
        # Calculate the new ratings after removing the review
        knowledge_rating = teacher.knowledge_rating
        teaching_skill_rating = teacher.teaching_skill_rating
        easiness_rating = teacher.easiness_rating
        communication_rating = teacher.communication_rating
        review_count = teacher.review_count
        review_knowledge_rating = instance.knowledge_rating
        review_teaching_skill_rating = instance.teaching_skill_rating
        review_easiness_rating = instance.easiness_rating
        review_communication_rating = instance.communication_rating

        total_ratings = teacher.review_count - 1
        new_teacher_knowledge_rating = (knowledge_rating * review_count - review_knowledge_rating) / total_ratings
        new_teacher_teaching_skill_rating = (
                                                    teaching_skill_rating * review_count - review_teaching_skill_rating) / total_ratings
        new_teacher_easiness_rating = (easiness_rating * review_count - review_easiness_rating) / total_ratings
        new_teacher_communication_rating = (
                                                   communication_rating * review_count - review_communication_rating) / total_ratings
        new_teacher_avg_rating = (new_teacher_communication_rating + new_teacher_easiness_rating +
                                  new_teacher_teaching_skill_rating + new_teacher_knowledge_rating) / 4

        teacher.easiness_rating = new_teacher_easiness_rating
        teacher.teaching_skill_rating = new_teacher_teaching_skill_rating
        teacher.communication_rating = new_teacher_communication_rating
        teacher.knowledge_rating = new_teacher_knowledge_rating
        teacher.avg_rating = new_teacher_avg_rating
        teacher.review_count = total_ratings
    else:
        # If there are no more reviews, reset all ratings and count to zero
        teacher.easiness_rating = 0
        teacher.teaching_skill_rating = 0
        teacher.communication_rating = 0
        teacher.knowledge_rating = 0
        teacher.avg_rating = 0
        teacher.review_count = 0

    teacher.save()


@receiver(pre_save, sender=Review)
def update_teacher_ratings_on_review(sender, instance, **kwargs):
    try:
        old_review = Review.objects.get(pk=instance.pk)
    except Review.DoesNotExist:
        old_review = None

    if old_review:
        if (
                instance.knowledge_rating != old_review.knowledge_rating or
                instance.teaching_skill_rating != old_review.teaching_skill_rating or
                instance.easiness_rating != old_review.easiness_rating or
                instance.communication_rating != old_review.communication_rating
        ):
            teacher = instance.teacher
            rating_names = (
                'knowledge_rating',
                'teaching_skill_rating',
                'easiness_rating',
                'communication_rating'
            )
            old_ratings = (
                old_review.knowledge_rating,
                old_review.teaching_skill_rating,
                old_review.easiness_rating,
                old_review.communication_rating
            )
            new_ratings = (
                instance.knowledge_rating,
                instance.teaching_skill_rating,
                instance.easiness_rating,
                instance.communication_rating
            )
            total_ratings = teacher.review_count
            for rating_name, old, new in zip(rating_names, old_ratings, new_ratings):
                if old != new:
                    recalc_rating = (getattr(teacher, rating_name) * total_ratings - old + new) / total_ratings
                    setattr(teacher, rating_name, recalc_rating)
            new_avg_rating = (teacher.communication_rating + teacher.easiness_rating + teacher.teaching_skill_rating +
                              teacher.knowledge_rating) / 4
            teacher.avg_rating = new_avg_rating
            teacher.save()
