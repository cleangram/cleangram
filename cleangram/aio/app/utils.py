import functools
import inspect


async def check_filters(event, filters, **kwargs):
    filter_kwargs = {}
    for fil in filters:
        if processed := functools.partial(fil, **kwargs)(event):
            if inspect.iscoroutine(processed):
                processed = await processed
            if isinstance(processed, dict):
                filter_kwargs.update(processed)
            if not processed:
                return
        else:
            return
    return filter_kwargs
