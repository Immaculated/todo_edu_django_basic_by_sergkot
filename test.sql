SELECT "main_listmodel"."id",
       "main_listmodel"."name",
       "main_listmodel"."created",
       "main_listmodel"."modified",
       "main_listmodel"."user_id",
       "main_listmodel"."is_done",
       "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
FROM "main_listmodel"
         INNER JOIN "auth_user" ON ("main_listmodel"."user_id" = "auth_user"."id")
WHERE "main_listmodel"."id" = 5
LIMIT 21