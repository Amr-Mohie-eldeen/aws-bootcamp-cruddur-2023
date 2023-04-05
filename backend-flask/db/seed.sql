INSERT INTO public.users (display_name, handle, cognito_user_id)
VALUES
  ('Andrew Brown', 'andrewbrown' ,'MOCK'),
  ('Andrew Bayko', 'bayko' ,'MOCK');

INSERT INTO public.users (display_name, handle, cognito_user_id,uuid)
VALUES 
  ('orcy', 'orcy','94b4de46-e9d1-41f4-9827-8bf3bc584691','50d211e7-a432-4bb7-8d2f-cfbb57cab7b8'),
  ('Amr', 'amrmohie','8109954e-1c23-45a0-a385-393277601495','a526bd87-96b8-4003-8b3e-d07765efa923');


INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  ) 