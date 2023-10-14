from django.db.models.signals import pre_save, post_save
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
                                  new_teacher_teaching_skill_rating + new_teacher_knowledge_rating)/4
        teacher.easiness_rating = new_teacher_easiness_rating
        teacher.teaching_skill_rating = new_teacher_teaching_skill_rating
        teacher.communication_rating = new_teacher_communication_rating
        teacher.knowledge_rating = new_teacher_knowledge_rating
        teacher.avg_rating = new_teacher_avg_rating
        teacher.review_count += 1
        teacher.save()
