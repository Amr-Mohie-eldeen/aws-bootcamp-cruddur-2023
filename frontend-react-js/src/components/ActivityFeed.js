import './ActivityFeed.css';
import ActivityItem from './ActivityItem';

export default function ActivityFeed(props) {
  console.log("User data in ActivityFeed AGAIN: ", props.user);
  return (
    <div className='activity_feed_collection'>
      {props.activities.map(activity => {
      return  <ActivityItem setReplyActivity={props.setReplyActivity} setPopped={props.setPopped} key={activity.uuid} activity={activity} user={props.user.cognito_user_uuid} />
      })}
    </div>
  );
}