import React, { useEffect, useRef } from "react";
import "./MessageFeed.css";
import MessageItem from "./MessageItem";

export default function MessageFeed(props) {
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "auto" });
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, [props.messages]);

  return (
    <div className="message_feed">
      <div className="message_feed_heading">
        <div className="title">Messages</div>
      </div>
      <div className="message_feed_collection">
        {props.messages.map((message, index) => {
          return (
            <MessageItem
              key={message.uuid}
              message={message}
              ref={index === props.messages.length - 1 ? messagesEndRef : null}
            />
          );
        })}
      </div>
    </div>
  );
}
