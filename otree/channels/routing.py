from channels.routing import route, route_class

from otree.channels import consumers
from otree.extensions import get_extensions_modules


channel_routing = [

    route('otree.create_session',
          consumers.create_session),

    # WebSockets
    route_class(
        consumers.WaitPage,
        path=r'^/otree1/wait_page/(?P<params>[\w,]+)/$'),
    route_class(
        consumers.GroupByArrivalTime,
        path=r'^/otree1/group_by_arrival_time/(?P<params>[\w,\.]+)/$'),
    route_class(
        consumers.AutoAdvance,
        path=r'^/otree1/auto_advance/(?P<params>[\w,]+)/$'),
    route_class(consumers.WaitForSession,
          path=r'^/otree1/wait_for_session/(?P<pre_create_id>\w+)/$'),
    route_class(
          consumers.RoomParticipant,
          path=r'^/otree1/wait_for_session_in_room/(?P<params>[\w,]+)/$'),
    route_class(
          consumers.RoomAdmin,
          path=r'^/otree1/room_without_session/(?P<room>\w+)/$'),
    route_class(
          consumers.BrowserBotsClient,
          path=r'^/otree1/browser_bots_client/(?P<session_code>\w+)/$'),
    route_class(
          consumers.BrowserBot,
          path=r'^/otree1/browser_bot_wait/$'),


]

for extensions_module in get_extensions_modules('routing'):
    channel_routing += getattr(extensions_module, 'channel_routing', [])
